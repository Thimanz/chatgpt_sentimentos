from fastapi import FastAPI
from ChatGPTRequestBody import ChatGPTRequestBody
from Evento import Evento
import requests
import chatgpt


def criar_endpoints(OPENAI_API_KEY):
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello, FastAPI"}

    @app.post("/sentimentos")
    async def root(chatGPTRequestBody: ChatGPTRequestBody):
        return chatgpt.encontrar_sentimento(OPENAI_API_KEY, chatGPTRequestBody)

    @app.post("/eventos")
    async def root(evento: Evento):
        def LembreteCriado(evento: Evento):
            evento.tipo = "LembreteAnalisado"
            evento.dados.sentimento = chatgpt.encontrar_sentimento(OPENAI_API_KEY, evento.dados.texto)
            requests.post("http://localhost:10000/eventos", json=dict(evento))
            
        funcoes = {"LembreteCriado": LembreteCriado}
        try:
            funcoes[evento.tipo](evento)
        except:
            pass
        
    return app
LembreteCriado