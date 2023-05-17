from fastapi import FastAPI
from ChatGPTRequestBody import ChatGPTRequestBody
import chatgpt


def criar_endpoints(OPENAI_API_KEY):
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello, FastAPI"}

    @app.post("/sentimentos")
    async def root(chatGPTRequestBody: ChatGPTRequestBody):
        return chatgpt.encontrar_sentimento(OPENAI_API_KEY, chatGPTRequestBody)

    return app
