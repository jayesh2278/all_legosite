import scrapy
import pandas as pd

class NoonComSpider(scrapy.Spider):
    name = 'noon_com'
    data = pd.read_excel('LEGO Price comparison Brief Links.xlsx')
    start_urls = [f'{row}' for row in data['links_noon.com']]

    def parse(self, response):
        price = response.xpath('//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/span[2]/div/text()[3]').get()
        if price == None:
            price = response.xpath('//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/span/div/text()[3]').get()
        yield {'price': price}