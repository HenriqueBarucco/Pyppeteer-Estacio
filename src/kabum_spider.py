import scrapy
from scrapy import Request
from src.entities.product import Product

class KabumSpider(scrapy.Spider):
    name = 'kabum'
    
    def __init__(self, produto='Placa de vídeo', *args, **kwargs):
        super(KabumSpider, self).__init__(*args, **kwargs)
        self.produto = produto
        self.produtos = list()
        self.start_urls = ['https://www.kabum.com.br/busca/%s?page_number=1&page_size=100&facet_filters=&sort=price' % produto]

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)
            
    def parse(self, response):
        pages = response.xpath('//*[@id="listing"]/div/div/div/div/div/main/div/a')
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'}
    
        for page in pages:
            yield response.follow(page, headers=headers, callback=self.parse_item)
            #yield Request(page, callback=self.parse_item)

        next_page_container = response.xpath('//*[@id="listingPagination"]/ul/li[13]/a')
        if len(next_page_container) > 0:
            yield response.follow(next_page_container[0], headers=headers, callback=self.parse)


    def parse_item(self, response):
        item = Product()

        item['url'] = response.url
            
        item['nome'] = response.xpath('//*[@id="__next"]/main/article/section/div[3]/div[1]/div/h1/text()').extract_first()
        
        try:
            item['duracao'] = response.xpath('//*[@id="cardAlertaOferta"]/div[1]/div/div/text()')
        except AttributeError:
            self.logger.debug('Falha ao extrair duração em %s', response.url)
            pass

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
        
        self.produtos.append(item)
        yield item