import scrapy
import logging
from scrapy import Request
from urllib.parse import urljoin
from src.entities.product import Product
from src.helpers.save_data import save_data

class KabumSpider(scrapy.Spider):
    name = 'kabum'
    
    logging.getLogger('scrapy').propagate = False
    
    produtos = list()
    
    def __init__(self, produto, *args, **kwargs):
        super(KabumSpider, self).__init__(*args, **kwargs)
        self.produto = produto
        self.start_urls = ['https://www.kabum.com.br/busca/%s' % produto]
        
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)
        
    def closed(self, spider):
        print("banana")
        save_data.productToXlsx(self.produtos,'/home/mauri/Área de Trabalho/teste')
            
    def parse(self, response):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'}
        # Construir a nova URL com os parâmetros desejados
        
        new_url = urljoin(response.url, f"?page_number=1&page_size=100&facet_filters=&sort=price")
        yield response.follow(new_url, headers=headers)
        
        pages = response.xpath('//*[@id="listing"]/div/div/div/div/div/main/div/a')

        for page in pages:
            yield response.follow(page, headers=headers, callback=self.parse_item)
            #yield Request(page, callback=self.parse_item)

        #next_page_container = response.xpath('//*[@id="listingPagination"]/ul')
        #button_href = response.xpath('//*[@id="listingPagination"]/ul/li[7]/a/@href').get()
        #print("NEXT PAGE CONTAINER", len(next_page_container))
        #if len(next_page_container) > 0:
        #    yield response.follow(button_href, headers=headers, callback=self.parse)

    def parse_item(self, response):
        item = Product()

        item['url'] = response.url
            
        
        item['nome'] = response.xpath('//*[@id="__next"]/main/article/section/div[3]/div[1]/div/h1/text()').extract_first()
        if item['nome'] is None:
            item['nome'] = response.xpath('//*[@id="__next"]/main/article/section/div[2]/div[1]/div/h1/text()').extract_first()
        
        try:
            item['duracao'] = response.xpath('//*[@id="cardAlertaOferta"]/div[1]/div/div/span/text()').extract()
        except AttributeError:
            self.logger.debug('Falha ao extrair duração em %s', response.url)
            pass
        
        item['duracao'] = response.xpath('//*[@id="cardAlertaOferta"]/div[1]/div/div/span').get()
        
        """ precos = {}
        
        precos['preco_normal'] = response.xpath('//*[@id="blocoValores"]/div[3]/b/text()').re(r'\d*\.*\d+\,\d+')
        precos['preco_desconto'] = response.xpath('//*[@id="blocoValores"]/div[2]/div[1]/h4/text()').re(r'\d*\.*\d+\,\d+')
        
        if len(precos['preco_normal']) > 0:
            try:
                item['preco_normal'] = response.xpath('//*[@id="blocoValores"]/div[2]/div[1]/h4/text()').extract()
            except AttributeError:
                self.logger.debug('Falha ao extrair preço normal em %s', response.url)
                pass """
        precos = {
            'preco_normal': response.xpath('//*[@id="blocoValores"]/div[3]/b/text()').re(r'\d*\.*\d+\,\d+'),
            'preco_desconto': response.xpath('//*[@id="blocoValores"]/div[2]/div[1]/h4/text()').re(r'\d*\.*\d+\,\d+')
        }

        for key in precos.keys():
            if len(precos[key]) > 0:
                item[key] = float(precos[key][0].replace('.','').replace(',','.'))
            else:
                self.logger.debug('{} not found on %s'.format(key), 
                    response.url)
                
        if precos['preco_normal'] is not float:
            precos['preco_normal'] = 'NA'
            print('preco normal nao encontrado')
        
        self.produtos.append(item)
        print(item)
        yield item