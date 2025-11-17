@echo off
chcp 65001 >nul
title AI 번역기 with TTS

echo 🌐 AI 번역기 with TTS 시작...
echo.

REM 가상환경 확인
if not exist "venv\" (
    echo ⚠️  가상환경이 없습니다. 생성 중...
    python -m venv venv
    echo ✅ 가상환경 생성 완료
)

REM 가상환경 활성화
echo 🔧 가상환경 활성화 중...
call venv\Scripts\activate.bat

REM 의존성 설치 확인
if not exist "venv\.installed" (
    echo 📦 의존성 패키지 설치 중...
    pip install -r requirements.txt
    type nul > venv\.installed
    echo ✅ 패키지 설치 완료
)

REM 필요한 디렉토리 생성
if not exist "static\audio\" mkdir static\audio

echo.
echo ✨ 애플리케이션 시작...
echo 🌍 브라우저에서 http://localhost:5000 으로 접속하세요
echo.
echo 종료하려면 Ctrl+C를 누르세요
echo.

REM Flask 애플리케이션 실행
python app.py

pause
