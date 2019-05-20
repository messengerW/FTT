# 好吧，试了好多次，暂时还不会直接在别的类里面使用这个类爬到的 urls，没办法只能通过先把
# 这个类爬到的 urls 写进 excel 里面 然后再在需要的类里面读取

import scrapy
import xlrd
import os
from xlutils.copy import copy

filepath = "C:/Users/mushr/Desktop/433/urls.xls"


class GetUrl(scrapy.Spider):
    name = 'spider_geturls2'

    allowed_domains = ['tzuqiu.cc']

    start_urls = ['http://www.tzuqiu.cc/teams/2/fixture.do', ]

    def parse(self, response):

        url_list1 = []  # 英超
        url_list2 = []  # 欧冠
        url_list3 = []  # 其他
        # 打开一个workbook
        rb = xlrd.open_workbook(filepath)
        wb = copy(rb)
        # 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
        sheet = wb.get_sheet(0)
        # 获取到当前页面的所有 tr
        tr_list = response.xpath("//table[@class='fiture team-fixture']//tbody[@id='fixture-body']/tr")
        print("============list len = ", (len(tr_list)))
        for i in range(0, len(tr_list)):
            m_tr = tr_list.pop(0)
            game_properties = m_tr.xpath(".//td[3]/a/@title").extract_first()
            if game_properties == '英超':
                next_url = m_tr.xpath(".//td[10]/a/@href").extract_first()
                url_list1.append(next_url)
                sheet.write(i, 0, next_url)
            elif game_properties == '欧冠':
                next_url = m_tr.xpath(".//td[10]/a/@href").extract_first()
                url_list2.append(next_url)
                sheet.write(i, 1, next_url)
            else:
                next_url = m_tr.xpath(".//td[10]/a/@href").extract_first()
                url_list3.append(next_url)
                sheet.write(i, 2, next_url)
        os.remove(filepath)
        wb.save(filepath)
