from fastapi import FastAPI
from Evento import Evento
import requests
import chatgpt
import re


def criar_endpoints(OPENAI_API_KEY):
    app = FastAPI()

    @app.post("/eventos")
    async def root(evento: Evento):
        def LembreteCriado(evento: Evento):
            evento.tipo = "LembreteAnalisado"
            while True: #enquanto o chatgpt nao entregar uma resposta válida
                sentimento = chatgpt.encontrar_sentimento(OPENAI_API_KEY, evento.dados.texto)
                sentimento = re.sub(r"\s"," ",sentimento) #remover enters
                sentimento = re.sub(r"[^A-Za-z]"," ",sentimento) #remover qualquer pontuacao
                sentimento = re.sub(r"(?i)\b(?!Positivo\b|Neutro\b|Negativo\b)\w+\b","",sentimento).strip() #remover qualquer palavra que nao seja de interesse e espaços em branco
                if sentimento != "":
                    break
            evento.dados.sentimento = sentimento
            requests.post("http://localhost:10000/eventos", data=evento.json(), headers={"Content-type": "application/json"})
            
        funcoes = {"LembreteCriado": LembreteCriado}

        try:
            funcoes[evento.tipo](evento)
        except:
            pass
        return {"msg": "ok"}

    return app