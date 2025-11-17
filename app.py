from flask import Flask, render_template, request, jsonify, send_file
from transformers import MarianMTModel, MarianTokenizer
import torch
import os
from datetime import datetime
import hashlib

app = Flask(__name__)

# 오디오 파일 저장 디렉토리
AUDIO_DIR = 'static/audio'
os.makedirs(AUDIO_DIR, exist_ok=True)

# 번역 모델 캐시
translation_models = {}

def load_translation_model(source_lang, target_lang):
    """번역 모델 로드 (캐싱)"""
    model_key = f"{source_lang}-{target_lang}"
    
    if model_key in translation_models:
        return translation_models[model_key]
    
    # Helsinki-NLP의 Opus-MT 모델 사용
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        translation_models[model_key] = (tokenizer, model)
        return tokenizer, model
    except Exception as e:
        print(f"모델 로드 실패: {e}")
        return None, None

def translate_text(text, source_lang, target_lang):
    """텍스트 번역"""
    tokenizer, model = load_translation_model(source_lang, target_lang)
    
    if tokenizer is None or model is None:
        return f"번역 모델을 찾을 수 없습니다: {source_lang} -> {target_lang}"
    
    # 텍스트 토큰화 및 번역
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    with torch.no_grad():
        translated = model.generate(**inputs)
    
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

def text_to_speech(text, language='en'):
    """Coqui TTS를 사용한 음성 합성"""
    try:
        from TTS.api import TTS
        
        # TTS 모델 초기화
        if language == 'ko':
            # 한국어 모델 (사용 가능한 경우)
            tts = TTS(model_name="tts_models/ko/cv/vits", progress_bar=False)
        else:
            # 영어 모델
            tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
        
        # 고유한 파일명 생성
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
        audio_filename = f"tts_{timestamp}_{text_hash}.wav"
        audio_path = os.path.join(AUDIO_DIR, audio_filename)
        
        # 음성 생성
        tts.tts_to_file(text=text, file_path=audio_path)
        
        return audio_filename
    except Exception as e:
        print(f"TTS 오류: {e}")
        return None

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """번역 API 엔드포인트"""
    data = request.json
    text = data.get('text', '')
    source_lang = data.get('source_lang', 'en')
    target_lang = data.get('target_lang', 'ko')
    use_tts = data.get('use_tts', False)
    
    if not text:
        return jsonify({'error': '텍스트를 입력해주세요'}), 400
    
    # 번역 수행
    translated_text = translate_text(text, source_lang, target_lang)
    
    response = {
        'original_text': text,
        'translated_text': translated_text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }
    
    # TTS 옵션이 활성화된 경우
    if use_tts:
        audio_file = text_to_speech(translated_text, target_lang)
        if audio_file:
            response['audio_url'] = f'/static/audio/{audio_file}'
    
    return jsonify(response)

@app.route('/available_languages')
def available_languages():
    """사용 가능한 언어 쌍 목록"""
    # 일반적으로 사용 가능한 언어 쌍들
    languages = {
        'en-ko': '영어 → 한국어',
        'ko-en': '한국어 → 영어',
        'en-es': '영어 → 스페인어',
        'es-en': '스페인어 → 영어',
        'en-fr': '영어 → 프랑스어',
        'fr-en': '프랑스어 → 영어',
        'en-de': '영어 → 독일어',
        'de-en': '독일어 → 영어',
        'en-ja': '영어 → 일본어',
        'ja-en': '일본어 → 영어',
        'en-zh': '영어 → 중국어',
        'zh-en': '중국어 → 영어',
    }
    return jsonify(languages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
