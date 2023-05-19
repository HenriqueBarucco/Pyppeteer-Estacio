from helpers.pyppeteer import NotSelenium as Browser
import asyncio

async def main():
    
    session = await Browser().openSession()

    #await session.login("@alunos.estacio.br", "")
    await session.getProducts()

asyncio.get_event_loop().run_until_complete(main())