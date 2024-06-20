import scrapy
import pandas as pd

class FirstcrySaSpider(scrapy.Spider):
    name = 'firstcry_sa'

    def start_requests(self):
        df = pd.read_excel("LEGO Price comparison Brief Links all.xlsx")
        
        start_urls = []
        for index, row in df.iterrows():
            product_name = row["Product Name EN"]
            product_number  = row['Product Number']
            url = row["links_firstcry_sa"]
            start_urls.append({"product_name": product_name, "url": url,"product_number":product_number})
        
        for url_dict in start_urls:
            yield scrapy.Request(url=url_dict["url"], callback=self.parse, meta={"product_name": url_dict["product_name"],"product_number":url_dict["product_number"]})

    def parse(self, response):
        name = response.meta.get('product_name')
        number = response.meta.get('product_number')
        price = response.xpath('//span[@id="prod_price"]/text()').get()
        # if price:
        #     price = int(float(price))
        # else:
        #     price = 0    
        yield {
            'product_name':name,
            'product_number': number,
            'price': price
            }   
