from src.helpers.pyppeteer import NotSelenium as Browser
from src.helpers.save_data import save_data
from src.helpers.whatsapp import WhatsAppAPI

import asyncio

async def getFile(person):
    session = await Browser().openSession()
    await session.login(str(person.email), str(person.password))
    await session.getFile()

async def app(person):
    # Faz o download do arquivo da Sala de Aula Estácio
    await getFile(person)
    
    # Extrai o arquivo .7z e salva o csv em vários arquivos
    data_treatment = save_data(
        seven_zip_file_path='./downloads/data.7z',
        directory='/excels',
        seven_csv='5m Sales Records.csv',
        desktop_path=person.dir)
    data_treatment.execute()
    
    # Envia mensagem de sucesso para o usuário
    WhatsAppAPI().sendMessage(str(person.phone))

def run_application(person):
    loop = asyncio.get_event_loop()
    task = app(person)
    loop.run_until_complete(task)