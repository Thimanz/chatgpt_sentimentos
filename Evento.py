from DadosLembrete import DadosLembrete
from pydantic import BaseModel
from DadosObservacao import DadosObservacao
from typing import Union, Any


class Evento(BaseModel):
    tipo: str
    dados: Union[DadosLembrete, DadosObservacao, Any]
