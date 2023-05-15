from pyppeteer import launch
import time

class NotSelenium:
    async def openSession(self):
        self.__browser = await launch()
        self.__page = await self.__browser.newPage()
        return self

    async def login(self, email, password):
        await self.__page.goto('https://estudante.estacio.br/login')

        btnLogin = await self.__page.waitForXPath('//*[@id="section-login"]/div/div/div[1]/section/div[1]/button', isIntersectingViewport=True)
        await btnLogin.click()
        
        time.sleep(5)
        await self.__page.screenshot({'path': '1-login.png'})

        inputEmail = await self.__page.waitForXPath('//*[@id="i0116"]', isIntersectingViewport=True)

        await inputEmail.type(email)
        
        time.sleep(5)
        await self.__page.screenshot({'path': '2-email.png'})
        btnNext = await self.__page.waitForXPath('//*[@id="idSIButton9"]', isIntersectingViewport=True)

        await btnNext.click()


        inputPassword = await self.__page.waitForXPath('//*[@id="i0118"]', isIntersectingViewport=True)

        await inputPassword.type(password)

        time.sleep(5)
        await self.__page.screenshot({'path': '3-senha.png'})

        btnNext = await self.__page.waitForXPath('//*[@id="idSIButton9"]', isIntersectingViewport=True)
        await btnNext.click()

        time.sleep(5)
        await self.__page.screenshot({'path': '4-no.png'})

        btnNo = await self.__page.waitForXPath('//*[@id="idBtn_Back"]', isIntersectingViewport=True)
        await btnNo.click()

        time.sleep(5)
        await self.__page.screenshot({'path': '5-saladeaula.png'})

    async def getFile(self):
        classCard = await self.__page.waitForXPath('//*[@id="card-entrega-ARA0066"]', timeout=60000)
        await classCard.click()

        time.sleep(5)
        await self.__page.screenshot({'path': '6-abrirmateria.png'})

        tema5Card = await self.__page.waitForXPath('//*[@id="temas-lista-topicos"]/li[5]/a', isIntersectingViewport=True, timeout=60000)
        time.sleep(10)
        await tema5Card.click()

        time.sleep(5)
        await self.__page.screenshot({'path': '7-abrirtema.png'})

        btnDownloadGrupo1 = self.__page.waitForXPath('//*[@id="acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9"]', isIntersectingViewport=True, timeout=60000)
        time.sleep(5)
        await btnDownloadGrupo1.click()

        self.__page.waitForDownload()

        await self.__page.screenshot({'path': '8-baixar.png'})


    async def finishSession(self):
        await self.__browser.close()