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
    name = scrapy.Field()
    no = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    num = scrapy.Field()
    info = scrapy.Field()


class PlayerItem(scrapy.Item):
    no = scrapy.Field()
    name = scrapy.Field()
    club = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()
    games = scrapy.Field()
    goals = scrapy.Field()


class ClubItem(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    turn = scrapy.Field()
    win = scrapy.Field()
    tie = scrapy.Field()
    lose = scrapy.Field()
    goals = scrapy.Field()
    fumble = scrapy.Field()
    delt = scrapy.Field()
    score = scrapy.Field()


class GameItem(scrapy.Item):
    turn = scrapy.Field()               # 轮次
    score = scrapy.Field()              # 比分
    date = scrapy.Field()               # 比赛日期
    possession = scrapy.Field()         # 控球率

    shot = scrapy.Field()               # 射门数，详细分为 5 类
    shot_1 = scrapy.Field()             # 阵地战
    shot_2 = scrapy.Field()             # 定位球
    shot_3 = scrapy.Field()             # 反击
    shot_4 = scrapy.Field()             # 点球
    shot_5 = scrapy.Field()             # 乌龙球
    shot_on_target = scrapy.Field()     # 射正数
    goals = scrapy.Field()              # 进球数

    # 这几个暂时还没有获取
    passes_number = scrapy.Field()      # 传球数
    passes_short = scrapy.Field()       # 短传
    passes_long = scrapy.Field()        # 长传
    passes_center = scrapy.Field()      # 传中
    passes_through = scrapy.Field()     # 直塞
    passes_completed = scrapy.Field()   # 传球成功率

    vs_win_rate = scrapy.Field()        # 对抗成功率
    guoren = scrapy.Field()             # 过人 md,这个真查不到
    intercept = scrapy.Field()          # 抢断数
    mark = scrapy.Field()               # 球队评分
