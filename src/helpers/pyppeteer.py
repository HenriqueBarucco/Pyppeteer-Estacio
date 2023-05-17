from pyppeteer import launch
import entities.xcode as xcode
import requests
import asyncio

class NotSelenium:
    async def openSession(self):
        self.__browser = await launch(executablePath='/usr/bin/google-chrome-stable', headless=True, args=['--no-sandbox'])
        self.__page = await self.__browser.newPage()
        await self.__page.goto('https://estudante.estacio.br/login')
        return self

    async def login(self, email, password):
        # Esperando o botão de login aparecer
        await self._waitAndClick(xcode.LOGIN_BUTTON)
        await self.__page.screenshot({'path': 'screenshots/1-login.png'})

        # Selecionar o campo de email
        await self._waitAndType(xcode.EMAIL_FORM, email)
        await self.__page.screenshot({'path': 'screenshots/2-email.png'})

        # Selecionar o botão de "Próximo"
        await self._waitAndClick(xcode.NEXT_BUTTON)

        # Selecionar o campo de senha
        await self._waitAndType(xcode.PASSWORD_FORM, password)
        await self.__page.screenshot({'path': 'screenshots/3-senha.png'})

        # Selecionar o botão de "Entrar"
        await self._waitAndClick(xcode.ENTER_BUTTON)
        await self.__page.screenshot({'path': 'screenshots/4-no.png'})

        # Selecionar o botão de "Não"
        await self._waitAndClick(xcode.NO_BUTTON)
        await self.__page.screenshot({'path': 'screenshots/5-saladeaula.png'})

    async def getFile(self):
        # Selecionar Card da matéria (Paradigmas de Python...)
        await self._waitAndClick(xcode.CARD_MATERIA)
        await self.__page.screenshot({'path': 'screenshots/6-abrirmateria.png'})

        # Selecionar o tema (Tema 5)
        await self._waitAndClick(xcode.TEMA_5)
        await self.__page.screenshot({'path': 'screenshots/7-abrirtema.png'})

        # Selecionar o arquivo para download (Grupo 1)
        await self.__page.waitFor(xcode.GRUPO_1)
        await self.__page.click(xcode.GRUPO_1)
        
        await self.__page.screenshot({'path': 'screenshots/8-baixar.png'})
        
        # Espere a resposta da requisição de download
        response = await self.__page.waitForResponse(lambda response: response.url.startswith('https://s3.amazonaws.com'))
        
        r = requests.get(response.url)

        # Salve o arquivo
        with open('./downloads/data.7z', 'wb') as f:
            f.write(r.content)
            
    async def _waitAndClick(self, xcode):
        await self.__page.waitFor(xcode)
        await self.__page.click(xcode)
        await asyncio.sleep(5)
        
    async def _waitAndType(self, xcode, input):
        await self.__page.waitFor(xcode)
        await self.__page.type(xcode, input)
        await asyncio.sleep(5)

    async def finishSession(self):
        await self.__browser.close()