import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from HEBspider.items import HebspiderItem

class HEBspider(CrawlSpider):
    name = "HEB"
    allowed_domains = ["heb.com.mx"]
    start_urls = ["http://www.heb.com.mx/vinos-y-licores/cerveza.html"]
    
#    rules = (Rule(LinkExtractor(allow='heb\.com\.mx/vinos-y-licores/cerveza\.html\?p=[0-9][0-9]*$'), callback='parse_item', follow= True,),)
    
    rules = (Rule(LinkExtractor(allow='\?p=[1-9][0-9]*$'), callback='parse_item', follow= True,),)    

    def parse_item(self, response):
        for sel in response.xpath('''//div[@class = "product-info"]'''):
            item = HebspiderItem()
            item['titulo'] = sel.xpath('''h2[@class = "product-name"]/a/@title''').extract()
            item['link'] = sel.xpath('''h2[@class = "product-name"]/a/@href''').extract()
            item['marca']= sel.xpath('''span[@class = "marca-related"]/text()''').extract()
            item['precio'] = sel.xpath('''div[@class = "price-box"]/*/span[@class = "price"]/text()''').extract()
            yield item
