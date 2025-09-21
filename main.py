import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Lê a chave da variável "apikey" do .env
api_key = os.getenv("apikey")

# Inicializa o cliente com a chave
client = OpenAI(api_key=api_key)

# Gera a imagem
img = client.images.generate(
    model="gpt-image-1",
    prompt="um coelho",
    n=1,
    size="1024x1024"
)

# Converte de base64 e salva
image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
