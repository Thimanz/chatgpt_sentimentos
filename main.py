import os
import endpoints
from dotenv import load_dotenv

load_dotenv()

app = endpoints.criar_endpoints(os.getenv("OPENAI_API_KEY"))
