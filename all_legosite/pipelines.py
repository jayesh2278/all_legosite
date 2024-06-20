from itemadapter import ItemAdapter
import requests
from airtable import Airtable


#AIRTABLE_TOKEN = "patYFBetyADuQVmaB"
AIRTABLE_TOKEN = "patYFBetyADuQVmaB.f8ae454fef41f4cd28c7f5872ac877ce4f4daca359fbc06947eb95fda1121ed3"
AIRTABLE_BASE_ID = "appQGfKDrk8F5SjW8"
TABLE_NAME = "Main Table"
endpoint= f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_NAME}"
airtable = Airtable(AIRTABLE_BASE_ID,TABLE_NAME,AIRTABLE_TOKEN) 

class AllLegositePipeline:
        def process_item(self, item, spider):
                if spider.name == "amazon.ae":  
                        self.price_key = "Amazon.ae LCS"
                elif spider.name == "amazon2.ae":
                        self.price_key = "Amazon.ae"
                elif spider.name == 'firstcry.ae':
                        self.price_key = "Firstcry.ae"
                elif spider.name == 'lego.saudiblocks.com':    
                        self.price_key = "SaudiBlocks SAR"
                elif spider.name ==  "lego.yellowblocks.me":
                        self.price_key = "YellowBlocks"
                elif spider.name == 'toysrusmena.com':
                        self.price_key = "Toysrusmena"
                elif spider.name == "noon.ae":
                        self.price_key = "Noon.ae"
                elif spider.name == "amazon_sa":
                        self.price_key = "Amazon.sa"

                elif spider.name == 'firstcry_sa':
                        self.price_key = "Firstcry.sa"

                elif spider.name == "noon_saudien":
                        self.price_key = "Noon.saudien"


                adapter = ItemAdapter(item)
                product_number = int(adapter['product_number'])
                product_name = adapter['product_name']
                discount_price = float(adapter['discount_price'])
                price = float(adapter['price']) if adapter['price'] else int(adapter['price'])

                record = airtable.search('Product Number',product_number )
                if record:
                        id = record[0]['id']
                        self.update_to_airtable(id,price)
                else:
                        self.add_to_airtable(product_name,product_number,discount_price,price)
                return item 
        



        def add_to_airtable(self,product_name,product_number,discount_price,price):
                headers = {
                "Authorization":f"Bearer {AIRTABLE_TOKEN}" ,
                "Content-Type": "application/json"
                }
                data ={
                        "records": [
                        {
                        "fields": {
                        "Product Name": product_name,
                        "Product Number": product_number,
                        "Discount Price": discount_price,
                        self.price_key: price,
                                        }
                        }]
                }
                r = requests.post(endpoint,json=data,headers=headers) 

        def update_to_airtable(self,id,price):
                headers = {
                "Authorization":f"Bearer {AIRTABLE_TOKEN}" ,
                "Content-Type": "application/json"
                }
                data ={
                        "records": [
                        {
                        "id": str(id),
                        "fields": {
                        self.price_key: price,
                                }
                        }]
                }
                r = requests.patch(endpoint,json=data,headers=headers)               