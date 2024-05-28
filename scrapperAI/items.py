# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperaiItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

class AmazonaiItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_author = scrapy.Field()
    product_price = scrapy.Field()
    product_image = scrapy.Field()

class DarazaiItem(scrapy.Item):
    product_name = scrapy.Field()
    rating = scrapy.Field()
    total_sold = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    free_shipping = scrapy.Field()