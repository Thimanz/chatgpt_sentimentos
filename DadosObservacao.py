from pydantic import BaseModel


class DadosObservacao(BaseModel):
    id: str
    texto: str
    lembreteId: int
    status: str
    sentimento: str
