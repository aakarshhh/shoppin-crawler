import scrapy
from urllib.parse import urljoin
import tldextract
from urllib.parse import urlparse

def is_valid_url(url):
    """Check if the URL is valid and not a JavaScript or void link."""
    parsed = urlparse(url)
    return parsed.scheme in ('http', 'https') and not url.lower().startswith('javascript')

class ProductCrawler(scrapy.Spider):
    name = 'product_crawler'

    def __init__(self, domains=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [f"http://{domain}" for domain in domains]
        self.visited = set()
        self.product_patterns =  [
        "/product/", "/item/", "/sku/", "/id/", "/pid/", "/variant/", "/offer/",
        "/price/", "/p/", "/asin/", "/uid/", "/itm/", "/prdt/", "/dp/"
    ]

    def parse(self, response):
        domain = tldextract.extract(response.url).registered_domain

        for link in response.css('a::attr(href)').getall():
            absolute_url = urljoin(response.url, link)
            if absolute_url not in self.visited:
                self.visited.add(absolute_url)
                if self.is_product_url(absolute_url):
                    yield {'Domain': domain, 'ProductURL': absolute_url}
                else:
                    yield scrapy.Request(absolute_url, callback=self.parse)

    def is_product_url(self, url):
        """Checks if the URL matches common product page patterns."""
        return any(pattern in url for pattern in self.product_patterns)
