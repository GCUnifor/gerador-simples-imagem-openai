import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega a chave do .env
load_dotenv()
client = OpenAI(api_key=os.getenv("apikey"))

print("🔎 Listando modelos disponíveis na sua conta...\n")

models = client.models.list()

tem_imagem = False
for m in models.data:
    print(m.id)
    if m.id == "gpt-image-1":
        tem_imagem = True

print("\n✅ Verificação concluída!")
if tem_imagem:
    print("👉 O modelo gpt-image-1 já está habilitado na sua conta.")
else:
    print("⚠️ O modelo gpt-image-1 ainda não está habilitado. Aguarde alguns minutos e tente de novo.")
