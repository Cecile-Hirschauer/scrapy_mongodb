# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StackItem(Item):
    # For each question the client needs the title and URL
    title = Field()
    url = Field()
