// DOM 요소
const sourceText = document.getElementById('source-text');
const translatedText = document.getElementById('translated-text');
const sourceLang = document.getElementById('source-lang');
const targetLang = document.getElementById('target-lang');
const translateBtn = document.getElementById('translate-btn');
const clearBtn = document.getElementById('clear-btn');
const swapBtn = document.getElementById('swap-languages');
const useTTS = document.getElementById('use-tts');
const charCount = document.getElementById('char-count');
const statusMessage = document.getElementById('status-message');
const audioPlayer = document.getElementById('audio-player');
const ttsAudio = document.getElementById('tts-audio');

// 문자 수 카운터
sourceText.addEventListener('input', function() {
    const count = this.value.length;
    charCount.textContent = count;
    
    if (count > 500) {
        this.value = this.value.substring(0, 500);
        charCount.textContent = 500;
    }
});

// 언어 스왑 기능
swapBtn.addEventListener('click', function() {
    const temp = sourceLang.value;
    sourceLang.value = targetLang.value;
    targetLang.value = temp;
    
    // 텍스트도 스왑
    const tempText = sourceText.value;
    sourceText.value = translatedText.value;
    translatedText.value = tempText;
    
    updateCharCount();
});

// 번역 기능
translateBtn.addEventListener('click', async function() {
    const text = sourceText.value.trim();
    
    if (!text) {
        showStatus('번역할 텍스트를 입력해주세요.', 'error');
        return;
    }
    
    if (sourceLang.value === targetLang.value) {
        showStatus('원본 언어와 번역 언어가 같습니다.', 'error');
        return;
    }
    
    // 버튼 비활성화 및 로딩 표시
    setLoading(true);
    showStatus('번역 중입니다... 처음 사용 시 모델 다운로드로 시간이 걸릴 수 있습니다.', 'info');
    
    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                source_lang: sourceLang.value,
                target_lang: targetLang.value,
                use_tts: useTTS.checked
            })
        });
        
        if (!response.ok) {
            throw new Error('번역 요청이 실패했습니다.');
        }
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        // 번역 결과 표시
        translatedText.value = data.translated_text;
        
        // 오디오가 있는 경우 표시
        if (data.audio_url) {
            ttsAudio.src = data.audio_url;
            audioPlayer.style.display = 'block';
            showStatus('번역 및 음성 합성이 완료되었습니다!', 'success');
        } else {
            audioPlayer.style.display = 'none';
            showStatus('번역이 완료되었습니다!', 'success');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showStatus(`오류가 발생했습니다: ${error.message}`, 'error');
        translatedText.value = '';
        audioPlayer.style.display = 'none';
    } finally {
        setLoading(false);
    }
});

// 지우기 기능
clearBtn.addEventListener('click', function() {
    sourceText.value = '';
    translatedText.value = '';
    audioPlayer.style.display = 'none';
    updateCharCount();
    hideStatus();
});

// 엔터 키로 번역 (Ctrl/Cmd + Enter)
sourceText.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        translateBtn.click();
    }
});

// 유틸리티 함수들
function setLoading(isLoading) {
    translateBtn.disabled = isLoading;
    const btnText = translateBtn.querySelector('.btn-text');
    const spinner = translateBtn.querySelector('.spinner');
    
    if (isLoading) {
        btnText.style.display = 'none';
        spinner.style.display = 'inline-block';
    } else {
        btnText.style.display = 'inline-block';
        spinner.style.display = 'none';
    }
}

function showStatus(message, type) {
    statusMessage.textContent = message;
    statusMessage.className = `status-message ${type}`;
}

function hideStatus() {
    statusMessage.className = 'status-message';
}

function updateCharCount() {
    charCount.textContent = sourceText.value.length;
}

// 페이지 로드 시 초기화
document.addEventListener('DOMContentLoaded', function() {
    console.log('AI Translator with TTS initialized');
    updateCharCount();
});
