import scrapy

class Product(scrapy.Item):
    url = scrapy.Field() # URL do produto
    nome = scrapy.Field() # Nome do produto
    preco_normal = scrapy.Field() # Valor Real
    preco_desconto = scrapy.Field() # Valor Promocional a vista
    preco_desconto_normal = scrapy.Field() # Valor Real do Promocional
    status = scrapy.Field() # Status do produto