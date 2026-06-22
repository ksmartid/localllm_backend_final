import requests

url = "http://localhost:8000/chat"

payload = {
    "message": "FastAPI 백엔드가 Ollama와 연결되는 과정을 쉽게 설명해줘.",
    "model": "llama3.2:3b",
    "system_prompt": "너는 초보자를 돕는 AI 강사다.",
    "temperature": 0.5,
    "top_p": 0.9,
    "num_predict": 256,
}

response = requests.post(url, json=payload, timeout=240)
response.raise_for_status()

data = response.json()

print("클라이언트 테스트 앱(잠시만 기다리세요.):")
data = response.json()
print("모델명:", data["model"])
print("응답 시간:", data["elapsed_time"], "초")
print("모델 응답:")
print(data["message"])
