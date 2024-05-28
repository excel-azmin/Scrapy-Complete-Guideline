import scrapy
from ..items import AmazonaiItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1716879238&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0"]

    def parse(self, response):
        items = AmazonaiItem()
        all_books = response.css('.puisg-row')
        for book in all_books:
            product_name = book.css('.a-color-base.a-text-normal::text').extract()
            product_author = book.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
            product_author = ' '.join([author.strip() for author in product_author if author.strip()])
            product_price = book.css('.a-price span span::text').extract()
            product_price = ''.join(product_price)
            product_image = book.css('.s-image-optimized-rendering::attr(src)').extract()
            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_price'] = product_price
            items['product_image'] = product_image
            yield items
        next_page= response.css('.s-pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)