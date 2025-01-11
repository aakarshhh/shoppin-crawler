import os
import asyncio
from utils import read_domains, write_to_csv
from spiders.products import ProductCrawler
from scrapy.crawler import CrawlerProcess

def run_crawler(domains):
    process = CrawlerProcess({
        'FEEDS': {
            'output.csv': {'format': 'csv', 'overwrite': True},
        },
        'LOG_LEVEL': 'INFO'
    })
    process.crawl(ProductCrawler, domains=domains)
    process.start()

if __name__ == "__main__":
    input_file = 'domains.txt'
    output_file = 'output.csv'

    # Step 1: Read input domains
    domains = read_domains(input_file)

    # Step 2: Run the crawler
    run_crawler(domains)

    print(f"Scraping complete. Results saved in {output_file}")
