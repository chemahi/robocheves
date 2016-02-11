import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from soriana.items import SorianaItem #importar la clase SorianaItem



class SorianaSpider(CrawlSpider):
    name = "Soriana" #nombre unico
    allowed_domains = ["http://www1.soriana.com/"] #para que la arania no se salga de este dominio
    start_urls = ["http://www1.soriana.com/site/default.aspx?p=11030&px=1&nuor=0"] #en que sitio va a empezar la arania
                                                                                   #pueden ser varios sitios
    
    #despues definimos las reglas
    #rules = (Rule(LinkExtractor(allow='\?p=[1-9][0-9]*$'), callback='parse_item', follow= True,),)    

    def parse_item(self, response): 
        item = SorianaItem()
        item['descripcion'] = response.xpath('''//div[@class="txtarticulohome"]/text()''').extract()
        item['precio'] = response.xpath('''//div[@class="precioarticulohome"]/text()''').extract()
        item['link'] = response.xpath('''//div[@class="artDi3"]/a/@href''').extract()
        yield item
