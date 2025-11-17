# 🌐 AI 번역기 with TTS

Hugging Face Transformers와 Coqui TTS를 활용한 웹 기반 번역 및 음성 합성 애플리케이션입니다.

## ✨ 주요 기능

- 🔄 **다국어 번역**: 영어, 한국어, 스페인어, 프랑스어, 독일어, 일본어, 중국어 등 지원
- 🔊 **음성 합성(TTS)**: 번역된 텍스트를 음성으로 변환
- 💡 **직관적인 UI**: 사용하기 쉬운 웹 인터페이스
- ⚡ **실시간 번역**: 빠른 번역 처리
- 🎯 **모델 캐싱**: 한 번 로드된 모델을 재사용하여 성능 향상

## 🛠️ 기술 스택

- **백엔드**: Flask
- **번역 모델**: Hugging Face Transformers (Helsinki-NLP Opus-MT)
- **음성 합성**: Coqui TTS
- **프론트엔드**: HTML, CSS, JavaScript

## 📋 요구사항

- Python 3.8 이상
- 충분한 디스크 공간 (모델 다운로드용)

## 🚀 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/yourusername/translator-tts.git
cd translator-tts
```

### 2. 가상환경 생성 (권장)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행

```bash
python app.py
```

### 5. 브라우저에서 접속

```
http://localhost:5000
```

## 📖 사용 방법

1. **언어 선택**: 원본 언어와 번역할 언어를 선택합니다
2. **텍스트 입력**: 번역할 텍스트를 입력합니다 (최대 500자)
3. **옵션 설정**: '음성 합성 사용' 체크박스로 TTS 기능을 활성화/비활성화할 수 있습니다
4. **번역 실행**: '번역하기' 버튼을 클릭합니다
5. **결과 확인**: 번역 결과와 음성(활성화 시)을 확인합니다

### 단축키

- `Ctrl + Enter` (또는 `Cmd + Enter`): 번역 실행
- 언어 스왑 버튼 (⇄): 원본 언어와 번역 언어를 서로 바꿉니다

## 🌍 지원 언어

- 영어 (en)
- 한국어 (ko)
- 스페인어 (es)
- 프랑스어 (fr)
- 독일어 (de)
- 일본어 (ja)
- 중국어 (zh)

## 📁 프로젝트 구조

```
translator-tts/
├── app.py                 # Flask 메인 애플리케이션
├── requirements.txt       # Python 의존성 패키지
├── README.md             # 프로젝트 문서
├── templates/
│   └── index.html        # 메인 HTML 템플릿
├── static/
│   ├── css/
│   │   └── style.css     # 스타일시트
│   ├── js/
│   │   └── script.js     # JavaScript
│   └── audio/            # 생성된 오디오 파일 저장
└── .gitignore            # Git 무시 파일 목록
```

## ⚙️ 설정

### 모델 변경

`app.py`에서 사용할 번역 모델을 변경할 수 있습니다:

```python
# 기본값: Helsinki-NLP/opus-mt-{source_lang}-{target_lang}
model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
```

### TTS 모델 변경

```python
# 영어 모델 예시
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# 한국어 모델 예시
tts = TTS(model_name="tts_models/ko/cv/vits")
```

## 🔧 문제 해결

### 모델 다운로드가 느린 경우

처음 실행 시 모델이 자동으로 다운로드됩니다. 시간이 걸릴 수 있으니 기다려주세요.

### 메모리 부족 오류

- 가벼운 모델 사용 검토
- 시스템 메모리 확인 및 증설 고려

### 특정 언어 쌍이 작동하지 않는 경우

모든 언어 쌍이 지원되지 않을 수 있습니다. [Helsinki-NLP 모델 페이지](https://huggingface.co/Helsinki-NLP)에서 사용 가능한 모델을 확인하세요.

## 📝 주의사항

- 처음 번역 시 모델 다운로드로 인해 시간이 걸릴 수 있습니다
- 오디오 파일은 `static/audio/` 디렉토리에 저장됩니다
- 장시간 사용 시 디스크 공간을 확인하세요

## 🤝 기여

프로젝트 개선을 위한 기여를 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 라이선스

이 프로젝트는 오픈소스이며 자유롭게 사용할 수 있습니다.

## 🙏 감사

- [Hugging Face Transformers](https://huggingface.co/transformers)
- [Coqui TTS](https://github.com/coqui-ai/TTS)
- [Helsinki-NLP](https://huggingface.co/Helsinki-NLP)

## 📧 문의

문제나 제안사항이 있으시면 Issue를 등록해주세요.

---

Made with ❤️ using Hugging Face Transformers & Coqui TTS
