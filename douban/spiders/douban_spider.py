# -*- coding: utf-8 -*-

import scrapy
from scrapy import log
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from douban.items import DoubanBookItem

class DoubanSpider(CrawlSpider):
    name = 'douban'
    start_urls = [
    'http://book.douban.com/'
    ]
    allow_domains = [
    'book.douban.com'
    ]
    rules=[
        Rule(LinkExtractor(allow=(r'http://www.douban.com/tag/.+/\?focus=book'))),
        Rule(LinkExtractor(allow=(r'http://www.douban.com/link2/\?url=http://www.douban.com/tag/.+/book&type=tag_more&name=.+&focus=book&mod=book'))),
        Rule(LinkExtractor(allow=(r'http://www.douban.com/tag/.+/book\?start=\d+'))),
        Rule(LinkExtractor(allow=(r'http://book.douban.com/subject/\d+')), callback='parse_item'),      
    ]

    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanBookItem()

        infos = filter(lambda info: not info.startswith('\n'), sel.xpath('//div[@id="info"]/text()').extract())

        try:
            item['bookname'] = sel.xpath('//span[@property="v:itemreviewed"]/text()').extract()[0]
            item['bookauthor'] = sel.xpath('//a[@class=""]/text()').extract()[0]
            item['bookpress'] = infos[0]
            item['pressdate'] = infos[1]
            item['bookpages'] = infos[2]
            item['bookprice'] = infos[3]
            item['bookisbn'] = infos[5]
            item['bookcode'] = sel.xpath('//strong[@property="v:average"]/text()').extract()[0]

            item['bookprice'] = item['bookprice'].split('.')[0]
            item['bookcode'] = item['bookcode'].strip()
        except Exception as e:
            log.msg('Error Info: %s' % e, level=log.DEBUG)
            log.msg('Item: %s' % item, level=log.DEBUG)

        '''
        In [37]: infos = infos[]

         湖南文艺出版社
         2015-7-1
         192
         48.00元
         平装
         9787540471699

        '''

        return item