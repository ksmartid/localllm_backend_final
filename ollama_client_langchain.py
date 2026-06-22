import time

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


OLLAMA_BASE_URL = "http://localhost:11434"


def call_ollama_chat(
    message: str,
    model: str = "llama3.2:3b",
    system_prompt: str = "너는 초보자를 돕는 친절한 AI 강사다.",
    temperature: float = 0.7,
    top_p: float = 0.9,
    num_predict: int = 256,
):
    """LCEL 문법으로 Ollama Chat 모델을 호출하고 문자열 응답과 소요 시간을 반환한다."""

    # 1. Prompt Template 정의
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{system_prompt}"),
            ("human", "{message}"),
        ]
    )

    # 2. Ollama Chat Model 정의
    llm = ChatOllama(
        model=model,
        base_url=OLLAMA_BASE_URL,
        temperature=temperature,
        top_p=top_p,
        num_predict=num_predict,
    )

    # 3. Output Parser 정의
    output_parser = StrOutputParser()

    # 4. LCEL Chain 구성
    chain = prompt | llm | output_parser

    # 5. 실행 시간 측정
    start_time = time.perf_counter()

    response_text = chain.invoke(
        {
            "system_prompt": system_prompt,
            "message": message,
        }
    )

    elapsed_time = round(time.perf_counter() - start_time, 3)

    return {
        "model": model,
        "message": response_text,
        "elapsed_time": elapsed_time,
    }


if __name__ == "__main__":
    print("\n채팅 응답 테스트(결과를 기다려 주세요.):")

    result = call_ollama_chat(
        message="Local LLM이 무엇인지 초보자에게 설명해줘."
    )

    print("\n모델:", result["model"])
    print("소요 시간:", result["elapsed_time"], "초")
    print("응답:")
    print(result["message"])