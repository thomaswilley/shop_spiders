A couple simple spiders to capture product attriubutes as json.
--
Install:
```bash
# clone this repo & in same directory:
$ python3 -m virtualenv --no-site-packages --distribute venv
$ source venv/bin/activate (or venv/Scripts/activate on windows)
$ pip install -r requirements.txt
# then follow the two steps below
```

Generate a list of product codes, to feed into the next spider as input:
```bash
$ scrapy runspider product_codes_spider.py -o productcodes.json
```

Generate a dict containing product info:
```bash
$ scrapy runspider product_compare_spider.py -a product_codes=productcodes.json -o results.json
```
