from DadosLembrete import DadosLembrete
from pydantic import BaseModel

class Evento(BaseModel):
    tipo: str
    dados: DadosLembrete
