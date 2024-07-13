import scrapy


class NicotinePouchesSpider(scrapy.Spider):
    name = "nicotine_pouches"
    allowed_domains = ["haypp.com"]
    start_urls = ["https://haypp.com"]

    def parse(self, response):
        pass
