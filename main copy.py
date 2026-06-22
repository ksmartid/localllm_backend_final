from fastapi import FastAPI, HTTPException

from ollama_client import call_ollama_chat, get_ollama_models
from schemas import ChatRequest, ChatResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Local LLM Chat API",
    description="Ollama 기반 로컬 LLM 채팅 백엔드 API",
    version="0.1.0",
)

# 브라우저는 보안상 서로 다른 출처의 요청을 제한하기 때문에 설정 필요
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    
    # allow_origins=["http://localhost:5173", "https://example.com"] 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Local LLM Chat API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        return call_ollama_chat(
            message=request.message,
            model=request.model,
            system_prompt=request.system_prompt,
            temperature=request.temperature,
            top_p=request.top_p,
            num_predict=request.num_predict,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"채팅 처리 중 오류가 발생했습니다: {exc}"
        ) 

# model 목록 가져오기
@app.get("/models")
def list_models():
    try:
        models = get_ollama_models()
        return {"models": models}
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"모델 목록 조회 중 오류가 발생했습니다: {exc}"
        )
