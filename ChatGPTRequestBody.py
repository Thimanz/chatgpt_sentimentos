from pydantic import BaseModel


class ChatGPTRequestBody(BaseModel):
    prompt: str
