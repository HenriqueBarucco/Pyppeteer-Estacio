from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.kabum_spider import KabumSpider

def run_spider(produto):
    process = CrawlerProcess()
    process.crawl(KabumSpider, produto=produto)
    process.start()

if __name__ == "__main__":
    nome_do_produto = "placa"
    run_spider(produto=nome_do_produto)