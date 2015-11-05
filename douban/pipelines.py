# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors

from twisted.enterprise import adbapi
from scrapy import log

class DoubanPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = 'douban',
            user = 'root',
            passwd = '1235',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, conn, item):
        query_sql = 'SELECT isbn FROM bookinfo WHERE isbn="%s"' % item['bookisbn'].strip()
        try:
            rst = conn.execute(query_sql)
        except:
            log.msg('query_sql: %s' % query_sql, level=log.CRITICAL)
            rst = True

        if rst:
            log.msg("Item already stored in db:%s" % item,level=log.DEBUG)
        else:
            inert_sql = 'INSERT INTO bookinfo VALUES("%s","%s","%s","%s","%s","%s","%s","%s")' % (item['bookisbn'], item['bookname'], item['bookauthor'], item['bookpress'], item['bookpages'], item['bookprice'], item['pressdate'], item['bookcode'])
            conn.execute(inert_sql)

            log.msg("Item stored in db: %s" % item, level=log.DEBUG)
            
    def _handle_error(self, e):
        log.err(e)
