import os
from src.helpers.pyppeteer import NotSelenium as Browser
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    
    session = await Browser().openSession()

    await session.login(str(os.getenv('EMAIL')), str(os.getenv('SENHA')))
    await session.getFile()
    await session.finishSession()

asyncio.get_event_loop().run_until_complete(main())