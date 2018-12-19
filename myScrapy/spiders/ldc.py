# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
import json
import re
from myScrapy.items import MyScrapyItem
from scrapy.http import Request


class ldc(scrapy.Spider):
    name = 'ershoufang'
    baseURL = 'https://nj.lianjia.com/ershoufang/pg'

    offset_page = 1
    page_group_list = ['ea10000bp0ep50/',
                        'ea10000bp50ep100/',
                        'ea10000bp100ep120/',
                        'ea10000bp120ep140/',
                        'ea10000bp140ep160/',
                        'ea10000bp160ep180/',
                        'ea10000bp180ep200/',
                        'ea10000bp200ep250/',
                        'ea10000bp250ep300/',
                        'ea10000bp300ep10000/']

    # 重写start_requests方法实现动态入口
    def start_requests(self):
        for i in self.page_group_list:
            url = self.baseURL + str(self.offset_page) + i
            yield Request(url, callback=self.parse)


    def parse(self, response):
        maxnum_dict = json.loads(response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract()[0])
        # 最大页数
        maxnum = int(maxnum_dict['totalPage'])
        for num in range(1,maxnum+1):
            split_str = self.baseURL + str(num)
            url = split_str + response.url.split(self.baseURL + str(self.offset_page))[1]
            yield Request(url, self.get_link, dont_filter=True)
        # yield Request('https://nj.lianjia.com/ershoufang/pg2/',self.get_link,dont_filter=True)


    def get_link(self,response):
        # node_list = response.xpath("//div[@class='info']/div[@class='title']/a")
        node_list = response.xpath("//div[@class='info clear']/div[@class='title']/a")
        for node in node_list:
            item = MyScrapyItem()
            item['houselink'] = node.xpath("./@href").extract()[0]
            yield scrapy.Request(item['houselink'], callback=self.parse_content, meta={'key': item})


    def parse_content(self,response):
        item = response.meta['key']
          # 所在区域
        # try:
        #     location = response.xpath("//div[@class='overview']//div[@class='content']//div[@class='areaName']/span").extract()[0].strip().join(response.xpath("//div[@class='overview']//div[@class='content']//div[@class='areaName']/span").extract()[1].strip()).encode('utf-8')
        #     print('location',location)
        #     item['location'] = location
        # except:
        #     item['location'] = 'None'


        #   小区名称
        try:
            hoursename = response.xpath("//div[@class='overview']//div[@class='content']//div[@class='communityName']/a/text()").extract()[0].strip()
            print(hoursename)
            item['housename'] = hoursename
        except:
            item['housename'] = 'None'

        #   所在楼层
        try:
            floorlevels = response.xpath("//div[@class='base']//ul/li[2]/text()").extract()[0].strip()
            # print('floorlevels',floorlevels)
            item['floorlevels'] = floorlevels
        except:
            item['floorlevels'] = 'None'


            #        挂牌总价
        try:
            totalprice = ''.join(response.xpath("//div[@class='overview']//div[@class='content']//div[@class='price ']/span/text()").extract())
            # print('totalprice',totalprice)
            item['totalprice'] = totalprice
        except:
            item['totalprice'] = 'None'

            #       单价
        try:
            unitprice = ''.join(response.xpath("//div[@class='overview']//div[@class='content']//div[@class='unitPrice']/span/text()").extract())
            # print('unitprice',unitprice)
            item['unitprice'] = unitprice
        except:
            item['unitprice'] = 'None'


            #        房屋户型
        try:
            housetype = response.xpath("//div[@class='base']//ul/li[1]/text()").extract()[0].strip()
            # print('housetype',housetype)
            item['housetype'] = housetype
        except:
            item['housetype'] = 'None'

            #        建筑面积
        try:
            constructarea = response.xpath("//div[@class='base']//ul/li[3]/text()").extract()[0].strip()
            # print('constructarea',constructarea)
            item['constructarea'] = constructarea
        except:
            item['constructarea'] = 'None'

            #       户型结构
        try:
            hourse_construction = response.xpath("//div[@class='base']//ul/li[4]/text()").extract()[0].strip()
            # print('hourse_construction',hourse_construction)
            item['hourse_construction'] = hourse_construction
        except:
            item['hourse_construction'] = 'None'

            #        套内面积
        try:
            housearea = response.xpath("//div[@class='base']//ul/li[5]/text()").extract()[0].strip()
            # print('housearea',housearea)
            item['housearea'] = housearea
        except:
            item['housearea'] = 'None'

        #        建筑类型
        try:
            building_types = response.xpath("//div[@class='base']//ul/li[6]/text()").extract()[0].strip()
            # print('building_types',building_types)
            item['building_types'] = building_types
        except:
            item['building_types'] = 'None'

        #        梯户比率
        try:
            lift_user_ratio = response.xpath("//div[@class='base']//ul/li[10]/text()").extract()[0].strip()
            # print('lift_user_ratio',lift_user_ratio)
            item['lift_user_ratio'] = lift_user_ratio
        except:
            item['lift_user_ratio'] = 'None'

        #        产权年限
        try:
            propertylimit = response.xpath("//div[@class='base']//ul/li[12]/text()").extract()[0].strip()
            # print('propertylimit',propertylimit)
            item['propertylimit'] = propertylimit
        except:
            item['propertylimit'] = 'None'

            # //div[@class='transaction']//ul/li[1]

        #        挂牌时间
        try:
            sale_time = response.xpath("//div[@class='transaction']//ul/li[1]/text()").extract()[0].strip()
            # print('sale_time',sale_time)
            item['sale_time'] = sale_time
        except:
            item['sale_time'] = 'None'

        #     #        房屋用途
        # try:
        #     item['house_use'] = response.xpath(
        #         "//div[@class='introContent']/div[@class='transaction']/div[@class='content']/ul/li[4]/text()").extract()[
        #         0].strip()
        # except:
        #     item['house_use'] = 'None'
        #     #        交易属性
        # try:
        #     item['tradeproperty'] = response.xpath(
        #         "//div[@class='introContent']/div[@class='transaction']/div[@class='content']/ul/li[2]/text()").extract()[
        #         0].strip()
        # except:
        #     item['tradeproperty'] = 'None'
        #     #        关注次数
        # try:
        #     item['guanzhu'] = response.xpath("//div[@class='msg']/span[5]/label/text()").extract()[0].strip()
        # except:
        #     item['guanzhu'] = 'None'
        #     #        带看次数
        # try:
        #     item['daikan'] = response.xpath("//div[@class='msg']/span[4]/label/text()").extract()[0].strip()
        # except:
        #     item['daikan'] = 'None'
        #     #        行政区
        # try:
        #     pre_district = response.xpath("//section[@class='wrapper']/div[@class='deal-bread']/a[3]/text()").extract()[
        #         0].strip()
        #     pattern = u'(.*?)二手房成交价格'
        #     item['district'] = re.search(pattern, pre_district).group(1)
        # except:
        #     item['district'] = 'None'
        #     #        成交总价
        # try:
        #     item['selltotalprice'] = response.xpath("//span[@class='dealTotalPrice']/i/text()").extract()[0].strip()
        # except:
        #     item['selltotalprice'] = 'None'
        #     #        成交均价
        # try:
        #     item['sellunitprice'] = response.xpath("//div[@class='price']/b/text()").extract()[0].strip()
        # except:
        #     item['sellunitprice'] = 'None'
        #     #        成交时间
        # try:
        #     item['selltime'] = response.xpath(
        #         "//div[@id='chengjiao_record']/ul[@class='record_list']/li/p[@class='record_detail']/text()").extract()[
        #         0].split(u',')[-1]
        # except:
        #     item['selltime'] = 'None'
        yield item