from scrapy import Spider
from scrapy.selector import Selector
from ..items import StackItem


class StackSpider(Spider):
    name = "stack" # Defines the name of the Spider
    allowed_domains = ["stackoverflow.com"] # Contains the base-URLs for the allowed domains for the spider to crawl.
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ] # List of URLs for the spider to start crawling from. All subsequent URLs will start from the data that the spider downloads from the URLS in start_urls
    
    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        
        # We are iterating through the `questions` and assigning the `title` 
        # and `url` values from the scraped data. 
        # Be sure to test out the XPath selectors in the JavaScript Console 
        # within Chrome Developer Tools - e.g., `
        # $x('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/text()')` 
        # and `$x('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/@href')`
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
            