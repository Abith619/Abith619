import scrapy

# class ExtractUrls(scrapy.Spider):
	
name = "extract"				

def start_requests(self):
    
    urls = ['https://www.geeksforgeeks.org/', ]
    
    for url in urls:
        yield scrapy.Request(url = url, callback = self.parse)
        print(url)
start_requests()
