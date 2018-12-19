# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class MyScrapyItem(scrapy.Item):
    #   所在区域
    location = scrapy.Field()
    #   挂牌时间
    sale_time = scrapy.Field()
    #   梯户比率
    lift_user_ratio = scrapy.Field()
    #   建筑类型
    building_types = scrapy.Field()
    #   户型结构
    hourse_construction = scrapy.Field()
    # 所在楼层
    floorlevels = scrapy.Field()
    # 房屋名称
    housename = scrapy.Field()
    # 产权年限
    propertylimit = scrapy.Field()
    # 链接
    houselink = scrapy.Field()
    # 挂牌总价
    totalprice = scrapy.Field()
    # 单价
    unitprice = scrapy.Field()
    # 房屋户型
    housetype = scrapy.Field()
    # 建筑面积
    constructarea = scrapy.Field()
    # 套内面积
    housearea = scrapy.Field()
    # 楼层
    housefloor = scrapy.Field()
    # 房屋用途
    house_use = scrapy.Field()
    # 交易属性
    tradeproperty = scrapy.Field()
    # 关注次数
    guanzhu = scrapy.Field()
    # 带看次数
    daikan = scrapy.Field()
    # 所属行政区域
    district = scrapy.Field()
    # 成交总价
    selltotalprice = scrapy.Field()
    # 成交均价
    sellunitprice = scrapy.Field()
    # 成交时间
    selltime = scrapy.Field()
    # 成交周期
    sellperiod = scrapy.Field()
    # 小区均价
    villageunitprice = scrapy.Field()
    # 小区建成年代
    villagetime = scrapy.Field()