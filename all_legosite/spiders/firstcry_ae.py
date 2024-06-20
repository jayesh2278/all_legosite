import scrapy
import pandas as pd

class FirstcryAeSpider(scrapy.Spider):
    name = 'firstcry_ae'
    data = pd.read_excel('LEGO Price comparison Brief Links.xlsx')
    start_urls = [f'{row}' for row in data['links_firstcry_ae']]

    def parse(self, response):
        price = response.xpath('//*[@id="prod_price"]/text()').get()
        yield {'price': price}