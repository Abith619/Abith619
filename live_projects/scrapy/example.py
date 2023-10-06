import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["odoo.com"]
    start_urls = ["https://odoo.com"]

    def parse(self, response):
        pass
