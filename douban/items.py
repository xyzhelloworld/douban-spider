# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    bookname = scrapy.Field()
    bookisbn = scrapy.Field()
    pressdate = scrapy.Field()
    bookpress = scrapy.Field()
    bookpages = scrapy.Field()
    bookprice = scrapy.Field()
    bookauthor = scrapy.Field()
    bookcode = scrapy.Field()
