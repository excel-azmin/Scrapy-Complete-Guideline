import scrapy
from ..items import DarazaiItem

class DarazSpiderSpider(scrapy.Spider):
    name = "daraz_spider"
    allowed_domains = ["www.daraz.com.bd"]
    start_urls = ["https://www.daraz.com.bd/catalog/?q=coffee&_keyori=ss&from=input&spm=a2a0e.home.search.go.735212f7OczPc1"]

    def parse(self, response):
        items = DarazaiItem()
        product_name = response.css("#id-title::text").extract()
        # rating = response.css(".c3XbGJ::text").extract()
        # total_sold = response.css(".c3lr34::text").extract()
        # price = response.css(".c13VH6::text").extract()
        # image = response.css("._2GchKS img::attr(src)").extract()
        # free_shipping = response.css(".c2i43-::text").extract()

