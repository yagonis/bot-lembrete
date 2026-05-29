import os
import time
import schedule
from twilio.rest import Client

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def enviar_mensagem():
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Lembrete agendado para tomar remédio!',
            to='whatsapp:+5538984132481'
        )
        print(f"lembrete enviado com sucesso! SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar lembrete: {e}")

schedule.every().day.at("19:00").do(enviar_mensagem)

print("Bot de lembrete iniciado. Aguardando para enviar mensagens...")

while True:
    schedule.run_pending()
    time.sleep(1)
