
import scrapy
from scrapy1.scrapy1.items import Test2Item

class ClubsSpider(scrapy.Spider):
    name = 'spider_clubs'
    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/competitions/1/teamStats.do',]

    def parse(self, response):

        clubs = response.xpath("//*[@id='seasonSummary_wrapper']/table/tbody/tr")

        for club in clubs:
            club_item = Test2Item()
            # 射门数
            club_item['shoot_total'] = club.xpath("./td[3]/text()").extract_first()
            # 控球率
            club_item['possession'] = club.xpath("./td[5]/text()").extract_first()
            # 传球成功率
            club_item['pass_completed_rate'] = club.xpath("./td[6]/text()").extract_first()

            yield club_item
