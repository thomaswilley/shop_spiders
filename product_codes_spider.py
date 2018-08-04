import scrapy
import json

class ProductCodesSpider(scrapy.Spider):
    """generate list of all available product codes"""
    name = 'product_codes_spider'
    start_urls = ['http://shop.dellemc.com/sitemap.xml']

    def parse(self, response):
        response.selector.register_namespace('d', 'http://www.sitemaps.org/schemas/sitemap/0.9')

        product_codes = []

        for link in response.xpath('//d:loc/text()').extract():
            ix = link.find('/p/')
            if ix >= 0:
                pc = link[ix+len('/p/')::]
                product_codes.append(pc)

        yield { 'product_codes': product_codes }
