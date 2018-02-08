# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class Glassdoor1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	#testCompanyInfo = scrapy.Field()
    CompanyHQ = scrapy.Field()
    Size = scrapy.Field()
    Type = scrapy.Field()
    Industry = scrapy.Field()
    Revenue = scrapy.Field()
    Name = scrapy.Field()

