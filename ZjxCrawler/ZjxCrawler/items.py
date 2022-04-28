# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZjxcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    fund_name = scrapy.Field()
    address = scrapy.Field()
    pass
