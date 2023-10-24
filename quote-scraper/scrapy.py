import scrapy

# scrapy runspider scraper.py
class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = [f'https://ebank.mbbank.com.vn/cp/pl/login?returnUrl=%2F']