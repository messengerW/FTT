from pyecharts import Radar

radar = Radar("雷达图", "球员能力值")
radar_data1 = [[2926, 16, 15, 84.3, 0.5, 14, 7.81]]
radar_data2 = [[2777, 17, 10, 85.8, 0.4, 8, 7.61]]
schema = [("出场时间", 3500), ("进球", 30), ("助攻", 25), ("传球成功率", 100), ("争顶成功", 1), ("全场最佳", 25), ("综合得分", 10)]
radar.config(schema)
radar.add("阿扎尔", radar_data1)
radar.add("斯特林", radar_data2, item_color="#1C86EE")
radar.render("C:\\Users\\mushr\\Desktop\\433\\DVFiles\\radar.html")
