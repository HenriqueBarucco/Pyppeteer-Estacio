from pyppeteer import launch
from pyppeteer import errors
import asyncio

class NotSelenium:
    async def openSession(self):
        self.__browser = await launch()
        self.__page = await self.__browser.newPage()
        return self

    async def login(self, email, password):
        await self.__page.goto('https://estudante.estacio.br/login')

        btnLogin = await self.__page.waitForXPath('//*[@id="section-login"]/div/div/div[1]/section/div[1]/button', isIntersectingViewport=True)
        await btnLogin.click()
        
        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/1-login.png'})

        inputEmail = await self.__page.waitForXPath('//*[@id="i0116"]', isIntersectingViewport=True)

        await inputEmail.type(email)
        
        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/2-email.png'})
        btnNext = await self.__page.waitForXPath('//*[@id="idSIButton9"]', isIntersectingViewport=True)

        await btnNext.click()


        inputPassword = await self.__page.waitForXPath('//*[@id="i0118"]', isIntersectingViewport=True)

        await inputPassword.type(password)

        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/3-senha.png'})

        btnNext = await self.__page.waitForXPath('//*[@id="idSIButton9"]', isIntersectingViewport=True)
        await btnNext.click()

        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/4-no.png'})

        btnNo = await self.__page.waitForXPath('//*[@id="idBtn_Back"]', isIntersectingViewport=True)
        await btnNo.click()

        await asyncio.sleep(10)
        await self.__page.screenshot({'path': 'screenshots/5-saladeaula.png'})

    async def getFile(self):
        cardMateria = await self.__page.waitForXPath('//*[@id="card-entrega-ARA0066"]', timeout=60000)
        await cardMateria.click()

        await asyncio.sleep(10)
        await self.__page.screenshot({'path': 'screenshots/6-abrirmateria.png'})

        await asyncio.sleep(15)
        tema5Card = await self.__page.waitForXPath('//*[@id="temas-lista-topicos"]/li[5]', isIntersectingViewport=True, timeout=60000)
        await asyncio.sleep(5)
        await tema5Card.click()

        await asyncio.sleep(5)
        await self.__page.screenshot({'path': 'screenshots/7-abrirtema.png'})

        #btnDownloadGrupo1 = self.__page.waitForXPath('//*[@id="acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9"]', isIntersectingViewport=True, timeout=60000)
        #await asyncio.sleep(5)
        #await btnDownloadGrupo1.evaluate('node => node.click()', force_expr=True)

        #self.__page.waitForDownload()

    async def download_file(self):
        await self.__page.click('#acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9')
        await self.__page.screenshot({'path': 'screenshots/8-baixar.png'})
        
        # Interceptando o evento de download
        #client = await self.__page.target.createCDPSession()
        #await client.send('Page.enable')
        #download_event = await client.waitForEvent('Page.downloadWillBegin')
        
        #self.__page.waitForDownload()

        # Interceptando o evento de download
        client = await self.__page.target.createCDPSession()
        await client.send('Page.enable')
        await client.send('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': '/'})
        
        def on_download_will_begin(event):
            print(event)
            
        client.on('Page.downloadWillBegin', on_download_will_begin)
        
        # Esperando o download ser concluído
        await asyncio.sleep(5)  # aguarda 5 segundos

    async def finishSession(self):
        await self.__browser.close()