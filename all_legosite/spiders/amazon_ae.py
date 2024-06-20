import scrapy
import pandas as pd

class AmazonAeSpider(scrapy.Spider):
    name = 'amazon_ae'
    allowed_domains = ['amazon_ae.com']
    # data = pd.read_excel('LEGO Price comparison Brief Links.xlsx')
    # start_urls = [f'{row}' for row in data['links_amazon_ae']]

    def start_requests(self):
        df = pd.read_excel("LEGO Price comparison Brief Links all.xlsx")
        
        start_urls = []
        for index, row in df.iterrows():
            product_name = row["Product Name EN"]
            product_number  = row['Product Number']
            url = row["links_amazon_ae"]
            start_urls.append({"product_name": product_name, "url": url,"product_number":product_number})
        
        for url_dict in start_urls:
            yield scrapy.Request(url=url_dict["url"], callback=self.parse, meta={"product_name": url_dict["product_name"],"product_number":url_dict["product_number"]})

    def parse(self, response):
        price = response.xpath("//*[@id='corePrice_feature_div']/div/span/span[1]/text()").get()
        name = response.meta.get('product_name')
        number = response.meta.get('product_number')
        yield {
            'product_name':name,
            'product_number': number,
            'price': price
            }