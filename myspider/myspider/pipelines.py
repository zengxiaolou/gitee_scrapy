# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pq
import pymongo
from scrapy import Item

# class MyspiderPipeline(object):
#     def __init__(self):
#         self.comm = pq.connect(host='localhost', user='root', passwd='123456', db='scrapy', charset='utf8')
#         self.cur = self.comm.cursor()
#
#     def process_item(self, item, spider):
#         list_num = item.get('list_num')
#         pic = item.get('pic')
#         name = item.get('name')
#         comment = item.get('comment')
#         publisher_info = item.get('publisher_info')
#
#         sql = "insert into dangdang(list_num, pic, name, comment, publisher_info) values  (%s, %s, %s, %s, %s)"
#         self.cur.execute(sql, (list_num, pic, name, comment, publisher_info))
#         self.comm.commit()
#
#     def close_spider(self, spider):
#         self.cur.close()
#         self.comm.close()

# class BookSpiderPipeline(object):
#     def process_item(self, item, spider):
#         print(item)
#         pass


class MongoDBPipeline(object):
    """
    将item写入到MongoDB中
    """
    @classmethod
    def from_crawler(cls, crawler):
        # 访问配置文件取mongdb的url和name，如果没有则使用默认值
        cls.DB_URL = crawler.settings.get('MONGO_DB_URI', 'mongodb://localhost:27017')
        cls.DB_NAME = crawler.settings.get("MONGO_DB_NAME", "scrapy_data")
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        try:
            c = item['title']
            collection.insert_one(post)
            return item
        except:
            return item
