# 2019.05.13
# 爬取英超联赛20支球队38轮联赛的详细数据

import scrapy
from scrapy1.items import GameItem


class GameSpider(scrapy.Spider):
    name = 'spider_game'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/teams/11/fixture.do']

    def parse(self, response):
        # 首先找到每一条比赛信息的 tr
        game_list = response.xpath("//*[@id='fixture-body']/tr")
        # 然后筛选，舍弃杯赛，只要联赛。不过我觉得可以先全都爬下来，然后在数据库里面筛选
        for i_item in game_list:
            game_item = GameItem()
            game_item['date'] = i_item.xpath(".//td[4]/text()").extract_first()
            link = i_item.xpath(".//td[10]/a/@href").extract_first()
            print("========"+link)


            yield game_item

        # 获取下一页的链接//*[@id="fixture-body"]/tr[1]/td[10]/a
        info_link = response.xpath("//tr[@matchid]/td[10]/a/@href/text()").extract_first()
        print(info_link)
