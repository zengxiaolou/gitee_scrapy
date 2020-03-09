# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader


class DangDangItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class DangDang(scrapy.Item):
    list_num = scrapy.Field()
    pic = scrapy.Field()
    name = scrapy.Field()
    comment = scrapy.Field()
    publisher_info = scrapy.Field()


class BookItemLoader(ItemLoader):
    # default_output_processor = TakeFirst()
    pass


class BookItem(scrapy.Item):
    img = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()


class BossItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class BossItem(scrapy.Item):
    job_area = scrapy.Field()
    job_limit = scrapy.Field()
    salary = scrapy.Field()
    company_name = scrapy.Field()
    company_logo = scrapy.Field()
    tags = scrapy.Field()


class GiteeItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class GiteeItem(scrapy.Item):
    category =scrapy.Field()
    avatar = scrapy.Field()
    title = scrapy.Field()
    gvp = scrapy.Field()
    lang = scrapy.Field()
    label = scrapy.Field()
    watch = scrapy.Field()
    fork = scrapy.Field()
    star = scrapy.Field()
    desc = scrapy.Field()
    latest = scrapy.Field()