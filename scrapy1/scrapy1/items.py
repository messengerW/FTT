# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()

class DetailItem(scrapy.Item):
    # 抓取内容：1.帖子标题；2.帖子作者；3.帖子回复数
    title = scrapy.Field()
    author = scrapy.Field()
    reply = scrapy.Field()

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    no = scrapy.Field()
    movie_name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    numbers = scrapy.Field()
    describe = scrapy.Field()