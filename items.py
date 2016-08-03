# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy.item import Item,Field


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=Field()
    status=Field()
    area=Field()
    method=Field()
    times=Field()
    avPrice=Field()
    bond=Field()
    facility=Field()
    address=Field()


    
