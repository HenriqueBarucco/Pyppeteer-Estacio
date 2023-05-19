from pyppeteer import launch
import src.entities.xcode as xcode
import asyncio
import requests

class NotSelenium:
    async def openSession(self):
        self.__browser = await launch(headless=True, args=['--no-sandbox'])
        self.__page = await self.__browser.newPage()
        await self.__page.goto('https://estudante.estacio.br/login')
        return self

    async def login(self, email, password):
        # Esperando o botão de login aparecer
        await self._waitAndClick(xcode.LOGIN_BUTTON)
        await self.__page.screenshot({'path': 'screenshots/1-login.png'})
        print('Botão de login clicado!')

        # Selecionar o campo de email
        await self._waitAndType(xcode.EMAIL_FORM, email)
        await self.__page.screenshot({'path': 'screenshots/2-email.png'})
        print('Email digitado!')

        # Selecionar o botão de "Próximo"
        await self._waitAndClick(xcode.NEXT_BUTTON)
        print('Botão de próximo clicado!')

        # Selecionar o campo de senha
        await self._waitAndType(xcode.PASSWORD_FORM, password)
        await self.__page.screenshot({'path': 'screenshots/3-senha.png'})
        print('Senha digitada!')

        # Selecionar o botão de "Entrar"
        await self._waitAndClick(xcode.ENTER_BUTTON)
        await self.__page.screenshot({'path': 'screenshots/4-no.png'})
        print('Botão de não clicado!')

        # Selecionar o botão de "Não"
        await self._waitAndClick(xcode.NO_BUTTON)
        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/5-saladeaula.png'})
        print('Sala de Aula aberta!')

    async def getFile(self):
        # Selecionar Card da matéria (Paradigmas de Python...)
        await self._waitAndClick(xcode.CARD_MATERIA)
        await self.__page.screenshot({'path': 'screenshots/6-abrirmateria.png'})
        print('Matéria aberta!')

        # Selecionar o tema (Tema 5)
        await self._waitAndClick(xcode.TEMA_5)
        await self.__page.screenshot({'path': 'screenshots/7-abrirtema.png'})
        print('Tema aberto!')

        # Selecionar o arquivo para download (Grupo 1)
        element = await self.__page.waitForXPath(xcode.GRUPO_1)
        await element.click()
        
        await self.__page.screenshot({'path': 'screenshots/8-baixar.png'})
        print('Iniciando download do arquivo 7z!')
        
        # Espere a resposta da requisição de download
        response = await self.__page.waitForResponse(lambda response: response.url.startswith('https://s3.amazonaws.com'))
        
        await self.__browser.close()
        
        r = requests.get(response.url)

        # Salve o arquivo
        with open('./downloads/data.7z', 'wb') as f:
            f.write(r.content)
            
        print('Arquivo 7z baixado!')
            
    async def _waitAndClick(self, xcode):
        element = await self.__page.waitForXPath(xcode)
        await element.click()
        await asyncio.sleep(5)
        
    async def _waitAndType(self, xcode, input):
        element = await self.__page.waitForXPath(xcode)
        await element.type(input)
        await asyncio.sleep(5)