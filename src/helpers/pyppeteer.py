from pyppeteer import launch
import asyncio

class NotSelenium:
    async def openSession(self):
        self.__browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
        self.__page = await self.__browser.newPage()
        return self

    async def login(self, email, password):
        await self.__page.goto('https://estudante.estacio.br/login')

        # Esperando o botão de login aparecer
        await self.__page.waitFor('#section-login > div > div > div.sc-cNNTdL.hItoDh.colLogin > section > div.sc-gKRMOK.hWvdtC > button')
        await self.__page.click('#section-login > div > div > div.sc-cNNTdL.hItoDh.colLogin > section > div.sc-gKRMOK.hWvdtC > button')

        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/1-login.png'})

        # Selecionar o campo de email
        await self.__page.waitFor('#i0116')
        await self.__page.type('#i0116', email)
        
        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/2-email.png'})

        # Selecionar o botão de "Próximo"
        await self.__page.waitFor('#idSIButton9')
        await self.__page.click('#idSIButton9')

        # Selecionar o campo de senha
        await self.__page.waitFor('#i0118')
        await self.__page.type('#i0118', password)

        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/3-senha.png'})

        # Selecionar o botão de "Entrar"
        await self.__page.waitFor('#idSIButton9')
        await self.__page.click('#idSIButton9')

        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/4-no.png'})

        # Selecionar o botão de "Não"
        await self.__page.waitFor('#idBtn_Back')
        await self.__page.click('#idBtn_Back')

        await asyncio.sleep(10)
        await self.__page.screenshot({'path': 'screenshots/5-saladeaula.png'})

    async def getFile(self):
        
        # Selecionar Card da matéria (Paradigmas de Python...)
        await self.__page.waitFor('#card-entrega-ARA0066')
        await self.__page.click('#card-entrega-ARA0066')

        await self.__page.screenshot({'path': 'screenshots/6-abrirmateria.png'})

        # Selecionar o tema (Tema 5)
        await self.__page.waitFor('#temas-lista-topicos > li:nth-child(5)')
        await self.__page.click('#temas-lista-topicos > li:nth-child(5)')
        
        await self.__page.screenshot({'path': 'screenshots/7-abrirtema.png'})

        # Selecionar o arquivo para download (Grupo 1)
        await self.__page.waitFor('#acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9')
        await self.__page.click('#acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9')
        
        await self.__page.screenshot({'path': 'screenshots/8-baixar.png'})

    async def finishSession(self):
        await self.__browser.close()