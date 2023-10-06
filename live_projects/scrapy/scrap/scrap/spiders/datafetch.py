import scrapy
from scrap.items import ScrapItem

class DatafetchSpider(scrapy.Spider):
    name = "datafetch"
    start_urls = [
        # 'https://www.paradisio-online.be/baby/kamers/neyt-vic',
        'https://www.paradisio-online.be/baby/kamers/bopita-lena'
    ]

    def parse(self, response):
        image_urls = response.css('.owl-carousel img::attr(src), img::attr(src)').extract()
        title = response.css('h1').extract()
        
        item = ScrapItem()

        indexes = [0, 2, 3, 4]
        item['image_urls'] = [response.urljoin(image_urls[i])for i in indexes]

        yield item

