import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import ScrapperaiItem


class QuotesLoginSpiderSpider(scrapy.Spider):
    name = "quotes_login_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(
            response,
            formdata={"csrf_token": token, "username": "abc", "password": "abc"},
            callback=self.start_scraping,
        )
    def start_scraping(self, response):
        items = ScrapperaiItem()
        open_in_browser(response)
        all_div_quotes = response.css("div.quote")
        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css(".tag::text").extract()
            items["title"] = title
            items["author"] = author
            items["tag"] = tag or 'No Tag'
            yield items
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.start_scraping)

        
