# 2019.05.13
# 爬取英超联赛20支球队38轮联赛的详细数据

import scrapy
import time
from scrapy1.items import GameItem


class GameSpider(scrapy.Spider):
    name = 'spider_game1'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/matches/52442/report.do',
                  'http://www.tzuqiu.cc/matches/52455/report.do',
                  'http://www.tzuqiu.cc/matches/52462/report.do',
                  'http://www.tzuqiu.cc/matches/52475/report.do',
                  'http://www.tzuqiu.cc/matches/52484/report.do',
                  'http://www.tzuqiu.cc/matches/52498/report.do',
                  'http://www.tzuqiu.cc/matches/52507/report.do',
                  'http://www.tzuqiu.cc/matches/52517/report.do',
                  'http://www.tzuqiu.cc/matches/52521/report.do',
                  'http://www.tzuqiu.cc/matches/52538/report.do',
                  'http://www.tzuqiu.cc/matches/52544/report.do',
                  'http://www.tzuqiu.cc/matches/52551/report.do',
                  'http://www.tzuqiu.cc/matches/52563/report.do',
                  'http://www.tzuqiu.cc/matches/52575/report.do',
                  'http://www.tzuqiu.cc/matches/52585/report.do',
                  'http://www.tzuqiu.cc/matches/52597/report.do',
                  'http://www.tzuqiu.cc/matches/52607/report.do',
                  'http://www.tzuqiu.cc/matches/52611/report.do',
                  'http://www.tzuqiu.cc/matches/52624/report.do',
                  'http://www.tzuqiu.cc/matches/52635/report.do',
                  'http://www.tzuqiu.cc/matches/52644/report.do',
                  'http://www.tzuqiu.cc/matches/52655/report.do',
                  'http://www.tzuqiu.cc/matches/52668/report.do',
                  'http://www.tzuqiu.cc/matches/52675/report.do',
                  'http://www.tzuqiu.cc/matches/52680/report.do',
                  'http://www.tzuqiu.cc/matches/52700/report.do',
                  'http://www.tzuqiu.cc/matches/52697/report.do',
                  'http://www.tzuqiu.cc/matches/52718/report.do',
                  'http://www.tzuqiu.cc/matches/52719/report.do',
                  'http://www.tzuqiu.cc/matches/52733/report.do',
                  'http://www.tzuqiu.cc/matches/52757/report.do',
                  'http://www.tzuqiu.cc/matches/52764/report.do',
                  'http://www.tzuqiu.cc/matches/52776/report.do',
                  'http://www.tzuqiu.cc/matches/52784/report.do',
                  'http://www.tzuqiu.cc/matches/52740/report.do',
                  'http://www.tzuqiu.cc/matches/52798/report.do',
                  'http://www.tzuqiu.cc/matches/52801/report.do',
                  'http://www.tzuqiu.cc/matches/52812/report.do',
                    ]

    def parse(self, response):
        game_item = GameItem()

        # 1.轮次
        turn = response.xpath("//td[@class='stat-box']/text()").extract_first()
        if turn:
            # strip()函数移除字符串头尾指定的字符（默认为空格或换行符），ps：对中间部分无效
            turn = turn.strip()
        else:
            turn = ' '
        game_item['turn'] = turn

        # 2.比分
        game_item['score'] = response.xpath("//td[@class='result']/text()").extract_first()

        # 3.比赛时间
        # 下面这句话有个坑，这个 tbody 有问题，加了就是空属性，不知道为什么。
        # //td[@class='match-info']//tbody/tr[5]/td[2]/text() 就会错，去掉tbody就没问题
        date_str = response.xpath("//td[@class='match-info']//tr[5]/td[2]/text()").extract_first()
        if date_str:
            date_str = ''.join(date_str.split())
            date_list = list(date_str)
            date_list.insert(10,' ')
            date = ''.join(date_list)
        else:
            date = 'nmsl'
        game_item['date'] = date

        # 4.控球率
        possession = response.xpath("//div[@class='sidebar-bkg sidebar-content']/div[1]/div[2]/div[2]/span/span[3]/span/text()").extract_first()
        if possession:
            possession = possession.strip()
        else:
            possession = ' '
        game_item['possession'] = possession

        # 5.射门数
        shot = response.xpath("//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[1]/span[3]/span/text()").extract_first()
        # wo kuai yao bei zhe ge gou bi xpath gao si le nmsl
        if shot:
            shot = shot.strip()
        else:
            shot = ' '
        game_item['shot'] = shot

        # 6.阵地战
        shot_1 = response.xpath("//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[2]/span[3]/span/text()").extract_first()
        # wo kuai yao bei zhe ge gou bi xpath gao si le nmsl
        if shot_1:
            shot_1 = shot_1.strip()
        else:
            shot_1 = ' '
        game_item['shot_1'] = shot_1

        # 7.定位球
        shot_2 = response.xpath("//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[3]/span[3]/span/text()").extract_first()
        # wo kuai yao bei zhe ge gou bi xpath gao si le nmsl
        if shot_2:
            shot_2 = shot_2.strip()
        else:
            shot_2 = ' '
        game_item['shot_2'] = shot_2

        # 8.反击
        shot_3 = response.xpath("//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[4]/span[3]/span/text()").extract_first()
        # wo kuai yao bei zhe ge gou bi xpath gao si le nmsl
        if shot_3:
            shot_3 = shot_3.strip()
        else:
            shot_3 = ' '
        game_item['shot_3'] = shot_3

        # 9.点球
        shot_4 = response.xpath("//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[5]/span[3]/span/text()").extract_first()
        # wo kuai yao bei zhe ge gou bi xpath gao si le nmsl
        if shot_4:
            shot_4 = shot_4.strip()
        else:
            shot_4 = ' '
        game_item['shot_4'] = shot_4

        # 10.乌龙球
        shot_5 = response.xpath("//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[6]/span[3]/span/text()").extract_first()
        # wo kuai yao bei zhe ge gou bi xpath gao si le nmsl
        if shot_5:
            shot_5 = shot_5.strip()
        else:
            shot_5 = ' '
        game_item['shot_5'] = shot_5

        # 11.射正数
        shot_on_target = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[2]/span[3]/span/text()").extract_first()
        if shot_on_target:
            shot_on_target = shot_on_target.strip()
        else:
            shot_on_target = ' '
        game_item['shot_on_target'] = shot_on_target

        # 12.传球成功率
        passes_completed = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[3]/span[3]/span/text()").extract_first()
        if passes_completed:
            passes_completed = passes_completed.strip()
        else:
            passes_completed = ' '
        game_item['passes_completed'] = passes_completed

        # 13.对抗成功率
        vs_win_rate = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[4]/span[3]/span/text()").extract_first()
        if vs_win_rate:
            vs_win_rate = vs_win_rate.strip()
        else:
            vs_win_rate = ' '
        game_item['vs_win_rate'] = vs_win_rate

        # 14.过人
        guoren = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[5]/span[3]/span/text()").extract_first()
        if guoren:
            guoren = guoren.strip()
        else:
            guoren = ' '
        game_item['guoren'] = guoren

        # 15.抢断
        intercept = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[6]/span[3]/span/text()").extract_first()
        if intercept:
            intercept = intercept.strip()
        else:
            intercept = ' '
        game_item['intercept'] = intercept

        # 16.球队评分
        mark = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[7]/span[3]/span/text()").extract_first()
        if mark:
            mark = mark.strip()
        else:
            mark = ' '
        game_item['mark'] = mark
        time.sleep(3)

        yield game_item
