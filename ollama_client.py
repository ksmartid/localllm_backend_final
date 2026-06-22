import time
import requests

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"

def call_ollama_chat(
    message,
    model="llama3.2:3b",
    system_prompt="너는 초보자를 돕는 친절한 AI 강사다.",
    temperature=0.7,
    top_p=0.9,
    num_predict=256,
):
    """Ollama Chat API를 호출하고 응답과 소요 시간을 반환한다."""

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        "stream": False,
        "think": False,
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        },
    }
    start_time = time.perf_counter()
    response = requests.post(
        OLLAMA_CHAT_URL,
        json=payload,
        timeout=180
    )
    response.raise_for_status()

    elapsed_time = round(time.perf_counter() - start_time, 3)
    data = response.json()

    return {
        "model": model,
        "message": data["message"]["content"],
        "elapsed_time": elapsed_time,
    }

def get_ollama_models():
    """Ollama에서 사용 가능한 모델 목록을 반환한다."""

    response = requests.get(
        OLLAMA_TAGS_URL,
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    models = data.get("models", [])

    return [model["name"] for model in models]


if __name__ == "__main__":
    print("\n채팅 응답 테스트(결과를 기다려 주세요.):")
    result = call_ollama_chat(message="Local LLM이 무엇인지 초보자에게 설명해줘.")
    print("\n모델:", result["model"])
    print("소요 시간:", result["elapsed_time"], "초")
    print("응답:")
    print(result["message"])

    models = get_ollama_models()
    print("사용 가능한 모델 목록:")
    print(models)
