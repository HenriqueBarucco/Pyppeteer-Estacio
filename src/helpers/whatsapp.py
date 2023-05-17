import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppAPI:
    def sendMessage(self, phone):
        print(f'Enviando mensagem para {phone}!')
        
        payload=f'id=55{phone}&message=Olá, o processo de extração do csv em Python acabou de finalizar!'
        
        headers = {
        'Authorization': f'Bearer {os.getenv("TOKEN")}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
        
        requests.request("POST", os.getenv("API"), headers=headers, data=payload.encode('utf-8'))