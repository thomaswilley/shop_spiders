import scrapy
import json

class ProductCompareSpider(scrapy.Spider):
    """
    generate product attributes by crawling product comparison
    usage: scrapy runspider -a product_codes='filename containing product codes' product_compare_spider.py
    """
    name = 'product_compare_spider'

    def load_product_codes(self, filename):
        with open(filename, 'r') as fin:
            product_codes = json.loads(fin.read())[0]['product_codes']
        return product_codes

    def __init__(self, product_codes=None, *args, **kwargs):
        # must have product codes to work from
        assert(product_codes != None)

        super(ProductCompareSpider, self).__init__(*args, **kwargs)
        if type(product_codes) == list:
            self.product_codes = product_codes
        else: # assume file..
            filename = product_codes
            self.product_codes = self.load_product_codes(filename)

    def start_requests(self):
        urls = ['https://shop.dellemc.com/en-us/productCompare?prodArray={}'.format(pc)
                for pc in self.product_codes]
        for i, url in enumerate(urls):
            pc = self.product_codes[i]
            yield scrapy.Request(url, meta={'product_code': pc})

    def parse(self, response):
        pc = response.meta['product_code']
        item = { pc: {}}

        for row in response.css('table.equaColumn > tr'):
            key = ''.join(row.css('th ::text').extract()).strip()

            if any(x in key for x in ['Spec Sheet', 'Data Sheet']):
                value = row.xpath('td/a/@href').extract_first()
            else:
                value = ''.join(row.css('td ::text').extract()).strip()
                value = '\r\n'.join([x.strip() for x in value.splitlines()])

            item[pc][key] = value

        yield item
