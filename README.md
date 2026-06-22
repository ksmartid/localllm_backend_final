# localllm_backend_final
localllm_backend_final
실행방법_localllm_backend_final_localllm_frontend_final

[1] localllm_backend_final 프로젝트 실행 방법(fastapi)


cd ~/localllm_backend_final
=====================
Linux / WSL에서 uv 설치
방법 1 (권장)
curl -LsSf https://astral.sh/uv/install.sh | sh
설치 후 적용:
source ~/.bashrc
버전 확인:
uv --version
------------------------------
Windows PowerShell에서 설치
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

설치 후:

uv --version
======================
pip로 설치
pip install uv

또는

python -m pip install uv
======================
주요 사용 명령어
가상환경 생성:
uv venv
가상환경 활성화:
source .venv/bin/activate

uv pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

fastapi dev main.py
http://127.0.0.1:8000/docs
-----------------------
requirements.txt 생성:
uv pip freeze > requirements.txt
===================


[2] localllm_frontend_final 프로젝트 실행 방법(react vite)
cd ~/localllm_frontend_final
node -v
npm -v
npm install
npm run dev
http://localhost:5173
