import scrapy

class Product(scrapy.Item):
    url = scrapy.Field() # URL do produto
    nome = scrapy.Field() # Nome do produto
    #marca = scrapy.Field() # Nome do produto
    preco_normal = scrapy.Field() # Valor Real
    preco_desconto = scrapy.Field() # Valor Promocional
    duracao = scrapy.Field() # Duração da promoção