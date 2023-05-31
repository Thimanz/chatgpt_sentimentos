from pydantic import BaseModel

class DadosLembrete(BaseModel):
    id: int
    texto: str
    status: str
    sentimento: str