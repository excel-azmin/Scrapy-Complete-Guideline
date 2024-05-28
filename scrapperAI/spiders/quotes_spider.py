import scrapy
from ..items import ScrapperaiItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        items = ScrapperaiItem()
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
        next_page = response.css('li.next a::attr(href)').get() 
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)   
        
        tags = response.css('li.next a::attr(href)').get()  
        for tag in tags:
            yield response.follow(tag, callback=self.parse_tags)
    # Scrap by tags
    def parse_tags(self, response):
        # Parse quotes on the tag-specific page
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            items = ScrapperaiItem()
            items['title'] = quote.css('span.text::text').extract_first()
            items['author'] = quote.css('.author::text').extract_first()
            items['tag'] = quote.css('.tag::text').extract()  # Get all tags
            yield items
        
        # Follow to next page within the tag if it exists
        next_page = response.css('li.next a::attr(href)').get() 
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_tags)
            