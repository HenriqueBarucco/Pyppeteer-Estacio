import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppAPI:
    def sendMessage(phone, message):
        print(f'Enviando mensagem para {phone}!')
        
        payload=f'id=55{phone}&message={message}'
        
        headers = {
        'Authorization': f'Bearer {os.getenv("TOKEN")}',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
        
        requests.request("POST", os.getenv("API") + '/text?key=henrique-bot', headers=headers, data=payload.encode('utf-8'))
        
    def sendFile(phone, filePath):
        print(f'Enviando mensagem para {phone}!')
        
        payload={'id': f'55{phone}', 'filename': 'Produtos.xlsx'}
        
        files=[
            ('file',('file',open(filePath,'rb'),'application/octet-stream'))
        ]
        
        headers = {
        'Authorization': f'Bearer {os.getenv("TOKEN")}',
        }
        
        requests.request("POST", os.getenv("API") + '/doc?key=henrique-bot', headers=headers, data=payload, files=files)