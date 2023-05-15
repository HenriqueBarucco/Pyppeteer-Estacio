from src.pyppeteer import NotSelenium as Browser
import asyncio

async def main():
    
    session = await Browser().openSession()

    await session.login('email', 'senha')
    await session.getFile()
    await session.finishSession()

asyncio.get_event_loop().run_until_complete(main())