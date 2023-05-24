from pydantic import BaseModel

class DadosLembrete(BaseModel):
    id: int
    texto: str
    sentimento: str