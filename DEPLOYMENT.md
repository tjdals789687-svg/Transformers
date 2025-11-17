# GitHub 배포 가이드

이 프로젝트를 GitHub에 업로드하고 배포하는 방법을 안내합니다.

## 📤 GitHub에 업로드하기

### 1. GitHub에서 새 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단의 `+` 버튼 클릭 → `New repository` 선택
3. Repository 이름 입력 (예: `ai-translator-tts`)
4. Public 또는 Private 선택
5. `Create repository` 클릭

### 2. 로컬에서 Git 초기화 및 업로드

```bash
# 프로젝트 디렉토리로 이동
cd translator-tts

# Git 초기화
git init

# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: AI Translator with TTS"

# GitHub 저장소 연결 (본인의 저장소 URL로 변경)
git remote add origin https://github.com/yourusername/ai-translator-tts.git

# 메인 브랜치로 변경 (필요한 경우)
git branch -M main

# GitHub에 푸시
git push -u origin main
```

## 🌐 웹에서 실행하기 (배포 옵션)

### 옵션 1: Render 배포 (무료)

1. [Render](https://render.com)에 회원가입
2. New → Web Service
3. GitHub 저장소 연결
4. 설정:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3
5. Create Web Service 클릭

### 옵션 2: Heroku 배포

1. `Procfile` 생성:
```
web: python app.py
```

2. `runtime.txt` 생성:
```
python-3.11.0
```

3. Heroku CLI로 배포:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### 옵션 3: Railway 배포

1. [Railway](https://railway.app)에 회원가입
2. New Project → Deploy from GitHub repo
3. 저장소 선택
4. 자동으로 배포 시작

### 옵션 4: PythonAnywhere

1. [PythonAnywhere](https://www.pythonanywhere.com) 가입
2. Web 탭에서 새 웹앱 생성
3. Flask 선택
4. 파일 업로드 및 설정

## ⚙️ 배포 시 주의사항

### 1. 환경 변수 설정

프로덕션 환경에서는 다음을 환경 변수로 설정하세요:

```python
# app.py 수정
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

### 2. 메모리 제한

무료 호스팅의 경우 메모리가 제한적입니다:
- 더 작은 모델 사용 고려
- 모델 캐시 제한 설정

### 3. 디스크 공간

오디오 파일이 계속 쌓이므로:
- 정기적으로 삭제하는 크론 작업 설정
- 또는 임시 파일로 처리

```python
# 오래된 파일 삭제 예시
import os
import time

def cleanup_old_audio_files(directory, max_age_hours=24):
    now = time.time()
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            age_hours = (now - os.path.getmtime(filepath)) / 3600
            if age_hours > max_age_hours:
                os.remove(filepath)
```

### 4. requirements.txt 최적화

배포 시간을 줄이기 위해 필요한 패키지만 포함:

```txt
flask==3.0.0
transformers==4.35.0
torch==2.1.0
sentencepiece==0.1.99
```

TTS가 필요 없다면 제외 가능합니다.

## 🚀 GitHub Pages (정적 버전)

백엔드 없이 프론트엔드만 배포하려면:

1. React나 Vue.js로 프론트엔드 재작성
2. Hugging Face Inference API 사용
3. GitHub Pages에 배포

```bash
git checkout -b gh-pages
# 빌드된 파일 추가
git push origin gh-pages
```

## 📱 GitHub Actions로 자동 배포

`.github/workflows/deploy.yml` 생성:

```yaml
name: Deploy to Render

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Render
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

## 🔒 보안 고려사항

1. API 키는 환경 변수로 관리
2. `.gitignore`에 민감한 파일 추가
3. HTTPS 사용 (대부분의 호스팅은 자동 제공)
4. Rate limiting 추가 고려

## 📊 모니터링

배포 후 모니터링:
- 로그 확인
- 에러 트래킹 (Sentry 등)
- 성능 모니터링

## 💡 팁

1. **무료 호스팅 한계**:
   - 메모리: 512MB ~ 1GB
   - CPU: 제한적
   - 큰 모델은 작동 안 될 수 있음

2. **최적화 방법**:
   - 모델 양자화 사용
   - 더 작은 모델 선택
   - 캐싱 적극 활용

3. **대안**:
   - Hugging Face Inference API 사용
   - Google Colab에서 실행
   - AWS/GCP의 무료 티어 활용

## 🆘 문제 해결

### 배포 실패 시

1. 로그 확인
2. 메모리 사용량 확인
3. requirements.txt 검증
4. Python 버전 확인

### 느린 응답 시

1. 더 작은 모델 사용
2. 모델 캐싱 확인
3. 서버 리소스 업그레이드

---

성공적인 배포를 기원합니다! 🎉
