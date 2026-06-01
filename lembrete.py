import os
from twilio.rest import Client
from dotenv import load_dotenv ##importante para carregar as variáveis da env

# Carrega as variáveis do arquivo .env
load_dotenv()

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def enviar_mensagem():
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Fala minha pretona manhsosa, vamo ta tomando remédinho do amor pq é importante! Te amo e um beijo do nego!',
            to='whatsapp:+553892509287'
        )
        print(f"lembrete enviado com sucesso! SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar lembrete: {e}")

if __name__ == "__main__":
    enviar_mensagem()
