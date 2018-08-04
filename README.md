shop_spiders
==============

A couple simple spiders to capture product attributes as json.

installation
---
```bash
# clone this repo & in same directory:
$ python3 -m virtualenv --no-site-packages --distribute venv
$ source venv/bin/activate (or venv/Scripts/activate on windows)
$ pip install -r requirements.txt
# then follow the two steps below
```

usage
---
```bash
# Generate a list of product codes, to feed into the next spider as input
$ scrapy runspider product_codes_spider.py -o productcodes.json
# Generate a dict containing product info, save off to results.json
$ scrapy runspider product_compare_spider.py -a product_codes=productcodes.json -o results.json
```

## author

Thomas Willey
- <https://github.com/thomaswilley>
- <https://twitter.com/thomaswilley>

## license

Open sourced under the [MIT license](LICENSE).
