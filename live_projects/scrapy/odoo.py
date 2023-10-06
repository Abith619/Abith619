import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class OdooSpider(CrawlSpider):
    name = "odoo"
    
    start_urls = ["https://www.paradisio-online.be/"]

    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = []
        
        title = response.css('title::text').extract_first()
        links = response.css('img::attr(src)').extract()
        for link in links:
            item.append(response.urljoin(link))
        yield{
            'image_urls':item
        }
        
