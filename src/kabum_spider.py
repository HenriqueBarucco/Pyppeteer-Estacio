import scrapy
import logging
from scrapy import Request
from scrapy_splash import SplashRequest
from urllib.parse import urljoin
from src.entities.product import Product
from src.helpers.save_data import save_data

class KabumSpider(scrapy.Spider):
    name = 'kabum'
    
    logging.getLogger('scrapy').propagate = False
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'}
    
    produtos = list()
    
    def __init__(self, produto, *args, **kwargs):
        super(KabumSpider, self).__init__(*args, **kwargs)
        self.produto = produto
        self.start_urls = ['https://www.kabum.com.br/busca/%s' % produto]
        
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)
        
    def closed(self, spider):
        save_data.productToXlsx(self.produtos,'E:\Henrique-PC\Desktop')
            
    def parse(self, response):
        new_url = urljoin(response.url, f"?page_number=1&page_size=100&facet_filters=&sort=price")
        yield response.follow(new_url, headers=self.headers)
        
        pages = response.xpath('//*[@id="listing"]/div/div/div/div/div/main/div/a')

        for page in pages:
            url = "https://www.kabum.com.br" + page.xpath('./@href').get()
            yield SplashRequest(url, self.parse_item, endpoint='render.html', args={'wait': 10}, headers=self.headers)


    def parse_item(self, response):
        item = Product()

        item['url'] = response.url

        item['nome'] = response.xpath('//*[@id="__next"]/main/article/section/div[3]/div[1]/div/h1/text()').extract_first()
        if item['nome'] is None:
            item['nome'] = response.xpath('//*[@id="__next"]/main/article/section/div[2]/div[1]/div/h1/text()').extract_first()

        promo_xpath = '//*[@id="cardAlertaOferta"]'
        normal_price_xpath = '//*[@id="blocoValores"]/div[2]/div[1]/span[1]/text()'
        discount_price_xpath = '//*[@id="blocoValores"]/div[2]/div[1]/h4/text()'
        non_discounted_price_xpath = '//*[@id="blocoValores"]/div[3]/b/text()'

        if response.xpath(promo_xpath):
            item['preco_normal'] = float(response.xpath(normal_price_xpath).re(r'\d*\.*\d+\,\d+')[0].replace('.','').replace(',','.'))
            item['preco_desconto'] = float(response.xpath(discount_price_xpath).re(r'\d*\.*\d+\,\d+')[0].replace('.','').replace(',','.'))
            item['preco_desconto_normal'] = float(response.xpath(non_discounted_price_xpath).re(r'\d*\.*\d+\,\d+')[0].replace('.','').replace(',','.'))
            item['duracao'] = response.xpath('//*[@id="cardAlertaOferta"]/div[1]/div/div/span/text()').extract_first()
            item['status'] = '✅'
        elif response.xpath(discount_price_xpath):
            item['preco_normal'] = float(response.xpath(discount_price_xpath).re(r'\d*\.*\d+\,\d+')[0].replace('.','').replace(',','.'))
            item['duracao'] = None
            item['preco_desconto'] = None
            item['preco_desconto_normal'] = None
            item['status'] = '✅'
        else:
            item['preco_normal'] = None
            item['duracao'] = None
            item['preco_desconto'] = None
            item['preco_desconto_normal'] = None
            item['status'] = '❌'

        self.produtos.append(item)
        print(item)