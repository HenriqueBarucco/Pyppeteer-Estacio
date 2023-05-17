import os
from helpers.pyppeteer import NotSelenium as Browser
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    
    session = await Browser().openSession()

    await session.login(str(os.getenv('EMAIL')), str(os.getenv('SENHA')))
    await session.getFile()
    await session.finishSession()
    
    # Unzip /downloads/data.7z
    
    # Tratar o csv em multiplos arquivos
    
    # Salvar no diretorio /excels
    
    # Enviar mensagem que o processo foi concluído

asyncio.get_event_loop().run_until_complete(main())

# str(os.getenv('EMAIL')), str(os.getenv('SENHA'))