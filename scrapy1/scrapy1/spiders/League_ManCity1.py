# ### 创建 2019.05.13
# 爬取英超联赛20支球队38轮联赛的详细数据
# ### 修改 2019.05.18 ctmd oj那道题截止了我还以为是明天截止 ctmdos ctmdry
# 命名方式 : 比赛性质_球队1/2( 1主场 2客场 )
# 其他所有英超联赛数据的爬虫都以此为模板

import scrapy
import time
from scrapy1.items import GameItem

class GameSpider(scrapy.Spider):
    name = 'spider_League_ManCity1'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/matches/52455/report.do',
                  'http://www.tzuqiu.cc/matches/52475/report.do',
                  'http://www.tzuqiu.cc/matches/52484/report.do',
                  'http://www.tzuqiu.cc/matches/52507/report.do',
                  'http://www.tzuqiu.cc/matches/52521/report.do',
                  'http://www.tzuqiu.cc/matches/52544/report.do',
                  'http://www.tzuqiu.cc/matches/52551/report.do',
                  'http://www.tzuqiu.cc/matches/52575/report.do',
                  'http://www.tzuqiu.cc/matches/52607/report.do',
                  'http://www.tzuqiu.cc/matches/52611/report.do',
                  'http://www.tzuqiu.cc/matches/52644/report.do',
                  'http://www.tzuqiu.cc/matches/52655/report.do',
                  'http://www.tzuqiu.cc/matches/52680/report.do',
                  'http://www.tzuqiu.cc/matches/52697/report.do',
                  'http://www.tzuqiu.cc/matches/52718/report.do',
                  'http://www.tzuqiu.cc/matches/52733/report.do',
                  'http://www.tzuqiu.cc/matches/52764/report.do',
                  'http://www.tzuqiu.cc/matches/52784/report.do',
                  'http://www.tzuqiu.cc/matches/52801/report.do',
                    ]

    def parse(self, response):

        game_item = GameItem()

        # 轮次
        turn = response.xpath("//td[@class='stat-box']/text()").extract_first()
        if turn:
            # strip()函数移除字符串头尾指定的字符（默认为空格或换行符），ps：对中间部分无效
            turn = turn.strip()
        else:
            turn = ' '
        game_item['turn'] = turn

        # 比赛时间
        # 下面这句话有个坑，这个 tbody 有问题，加了就是空属性，不知道为什么。
        # //td[@class='match-info']//tbody/tr[5]/td[2]/text() 就会错，去掉tbody就没问题
        date_str = response.xpath("//td[@class='match-info']//tr[5]/td[2]/text()").extract_first()
        if date_str:
            date_str = ''.join(date_str.split())
            date_list = list(date_str)
            date_list.insert(10, ' ')
            date = ''.join(date_list)
        else:
            date = ' '
        game_item['date'] = date

        # 比分
        game_item['score'] = response.xpath("//td[@class='result']/text()").extract_first()

        # 进球
        goals = response.xpath(
            "//div[@id='shotsTab']/div[2]/div[1]/div[3]/span[1]/span[4]/span/text()").extract_first()
        if goals:
            goals = goals.strip()
        else:
            goals = ' '
        game_item['goals'] = goals

        # 控球率
        possession = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[2]/div[2]/span/span[3]/span/text()").extract_first()
        if possession:
            possession = possession.strip()
        else:
            possession = ' '
        game_item['possession'] = possession

        # 对抗成功率
        confrontation_win_rate = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[4]/span[3]/span/text()").extract_first()
        if confrontation_win_rate:
            confrontation_win_rate = confrontation_win_rate.strip()
        else:
            confrontation_win_rate = ' '
        game_item['confrontation_win_rate'] = confrontation_win_rate

        # 过人
        beat_an_opponent = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[5]/span[3]/span/text()").extract_first()
        if beat_an_opponent:
            beat_an_opponent = beat_an_opponent.strip()
        else:
            beat_an_opponent = ' '
        game_item['beat_an_opponent'] = beat_an_opponent

        # 抢断
        intercept = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[6]/span[3]/span/text()").extract_first()
        if intercept:
            intercept = intercept.strip()
        else:
            intercept = ' '
        game_item['intercept'] = intercept

        # 球队评分
        mark = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[7]/span[3]/span/text()").extract_first()
        if mark:
            mark = mark.strip()
        else:
            mark = ' '
        game_item['mark'] = mark

        # 主客场 (手动填写)
        game_item['home_and_away'] = '主'

        # 射门数
        shot_number = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[1]/span[3]/span/text()").extract_first()
        if shot_number:
            shot_number = shot_number.strip()
        else:
            shot_number = ' '
        game_item['shot_number'] = shot_number

        # 阵地战
        shot_positional = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[2]/span[3]/span/text()").extract_first()
        if shot_positional:
            shot_positional = shot_positional.strip()
        else:
            shot_positional = ' '
        game_item['shot_positional'] = shot_positional

        # 定位球
        shot_placekick = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[3]/span[3]/span/text()").extract_first()
        if shot_placekick:
            shot_placekick = shot_placekick.strip()
        else:
            shot_placekick = ' '
        game_item['shot_placekick'] = shot_placekick

        # 反击
        shot_counterattack = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[4]/span[3]/span/text()").extract_first()
        if shot_counterattack:
            shot_counterattack = shot_counterattack.strip()
        else:
            shot_counterattack = ' '
        game_item['shot_counterattack'] = shot_counterattack

        # 点球
        shot_point = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[5]/span[3]/span/text()").extract_first()
        if shot_point:
            shot_point = shot_point.strip()
        else:
            shot_point = ' '
        game_item['shot_point'] = shot_point

        # 乌龙球
        shot_own = response.xpath(
            "//div[@id='shotsTab']/div[1]/div[2]/div[2]/div[6]/span[3]/span/text()").extract_first()
        if shot_own:
            shot_own = shot_own.strip()
        else:
            shot_own = ' '
        game_item['shot_own'] = shot_own

        # 射正数
        shot_on_target = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[2]/span[3]/span/text()").extract_first()
        if shot_on_target:
            shot_on_target = shot_on_target.strip()
        else:
            shot_on_target = ' '
        game_item['shot_on_target'] = shot_on_target

        # 传球数
        passes_number = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[1]/span[3]/span/text()").extract_first()
        if passes_number:
            passes_number = passes_number.strip()
        else:
            passes_number = ' '
        game_item['passes_number'] = passes_number

        # 短传
        passes_short = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[2]/span[3]/span/text()").extract_first()
        if passes_short:
            passes_short = passes_short.strip()
        else:
            passes_short = ' '
        game_item['passes_short'] = passes_short

        # 长传
        passes_long = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[3]/span[3]/span/text()").extract_first()
        if passes_long:
            passes_long = passes_long.strip()
        else:
            passes_long = ' '
        game_item['passes_long'] = passes_long

        # 传中
        passes_center = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[4]/span[3]/span/text()").extract_first()
        if passes_center:
            passes_center = passes_center.strip()
        else:
            passes_center = ' '
        game_item['passes_center'] = passes_center

        # 直塞
        passes_through = response.xpath(
            "//div[@id='passesTab']/div[1]/div[2]/div[2]/div[5]/span[3]/span/text()").extract_first()
        if passes_through:
            passes_through = passes_through.strip()
        else:
            passes_through = ' '
        game_item['passes_through'] = passes_through

        # 传球成功率
        passes_completed_rate = response.xpath(
            "//div[@class='sidebar-bkg sidebar-content']/div[1]/div[1]/div[3]/span[3]/span/text()").extract_first()
        if passes_completed_rate:
            passes_completed_rate = passes_completed_rate.strip()
        else:
            passes_completed_rate = ' '
        game_item['passes_completed_rate'] = passes_completed_rate

        time.sleep(3)
        yield game_item