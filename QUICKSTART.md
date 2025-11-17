# ⚡ 빠른 시작 가이드 (3분 완성!)

완전 초보자도 따라할 수 있는 가장 빠른 설치 방법입니다.

## 📝 체크리스트

시작하기 전에 확인하세요:
- [ ] Python이 설치되어 있나요? (없으면 1번 단계 실행)
- [ ] 프로젝트 파일을 다운로드했나요? (없으면 2번 단계 실행)
- [ ] 인터넷에 연결되어 있나요?

---

## 🎯 3단계로 끝내기

### 1단계: Python 설치 (이미 있으면 Skip!)

**Python 있는지 확인:**
```bash
python --version
```

**없거나 3.12 이상이면:**
1. https://www.python.org/downloads/release/python-3119/ 접속
2. **Windows installer (64-bit)** 다운로드
3. 설치할 때:
   - ⚠️ "Add Python to PATH" 체크 (중요!)
   - "Install Now" 클릭

---

### 2단계: 프로젝트 다운로드

**GitHub에서 다운로드:**
1. 프로젝트 페이지에서 **Code** 버튼 클릭
2. **Download ZIP** 클릭
3. 다운로드한 파일 압축 해제
4. `translator-tts` 폴더를 바탕화면으로 이동

---

### 3단계: 실행!

#### Windows 사용자 (제일 쉬움!)

**방법 A: 더블클릭으로 실행 (초간단!)**
1. `translator-tts` 폴더 열기
2. `run.bat` 파일 더블클릭
3. 검은 창이 뜨고 설치 진행 (5-10분)
4. "Running on http://127.0.0.1:5000" 메시지 나오면 성공!
5. 브라우저에서 `http://localhost:5000` 접속

**방법 B: 명령 프롬프트 사용**
```bash
# 1. 폴더로 이동 (바탕화면에 있다면)
cd Desktop\translator-tts

# 2. 가상환경 생성
py -3.11 -m venv venv

# 3. 가상환경 활성화
venv\Scripts\activate

# 4. 패키지 설치
pip install flask transformers torch sentencepiece protobuf TTS sacremoses

# 5. 실행!
python app.py
```

#### Mac/Linux 사용자

**터미널 열고 실행:**
```bash
# 1. 폴더로 이동
cd ~/Desktop/translator-tts

# 2. 실행 스크립트 권한 부여
chmod +x run.sh

# 3. 실행!
./run.sh
```

또는 수동 설치:
```bash
cd ~/Desktop/translator-tts
python3.11 -m venv venv
source venv/bin/activate
pip install flask transformers torch sentencepiece protobuf TTS sacremoses
python app.py
```

---

## 🎉 완료!

브라우저에서 **http://localhost:5000** 접속하면 번역기가 보입니다!

---

## ❓ 에러 해결 (자주 나는 것들)

### "python: command not found"
→ Python 설치 안 됨. 1단계로 돌아가기

### "Could not find TTS"
→ Python 버전이 3.12 이상. Python 3.11 설치 필요

### "torch==2.1.0 찾을 수 없음"
→ 이렇게 실행:
```bash
pip install flask transformers torch sentencepiece protobuf TTS sacremoses
```

### "Address already in use"
→ 5000번 포트가 사용 중. 다른 프로그램 종료하거나:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [번호] /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

### 스크립트 실행이 안 됨 (Windows PowerShell)
→ PowerShell을 관리자 권한으로 열고:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 💡 다음 번 실행할 때

**Windows:**
```bash
cd translator-tts
venv\Scripts\activate
python app.py
```

**Mac/Linux:**
```bash
cd translator-tts
source venv/bin/activate
python app.py
```

또는 그냥 `run.bat` (Windows) / `./run.sh` (Mac/Linux) 실행!

---

## 📚 더 자세한 내용은?

- **README.md**: 전체 가이드
- **DEPLOYMENT.md**: 온라인 배포 방법
- **GitHub Issues**: 문제 발생 시 질문

---

**축하합니다! 이제 AI 번역기를 사용할 준비가 되었습니다!** 🎊
