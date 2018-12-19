# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class MyscrapyPipeline(object):

    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = '/Users/haner/res.csv'
        # 打开(创建)文件
        self.file = open(store_file, 'wb')
        # csv写法
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        unitprice = ''.join(item['unitprice']).encode('utf-8').replace('\r', '').replace('\n', '').replace('\t', '')
        totalprice = ''.join(item['totalprice']).encode('utf-8').replace('\r', '').replace('\n', '').replace('\t', '')
        print(unitprice,'8888888888888888888888')
        print(item['houselink'],'77777777777777')
        print(totalprice,'8888888888888888888888')
        # 判断字段值不为空再写入文件
        # 写入顺序定义：
        # 链接;小区名称;所在区域;挂牌总价;单价;所在楼层;房屋户型;建筑面积;户型结构;套内面积;建筑类型;梯户比率;产权年限;挂牌时间
        if item['totalprice']:
            # self.writer.writerow((item['houselink'].encode('utf8'),item['totalprice'].encode('utf8'),item['unitprice'].encode('utf8')))
            self.writer.writerow((''.join(item['houselink'].encode('utf8', 'ignore')),
                                  ''.join(item['housename'].encode('utf8', 'ignore')),
                                  # ''.join(item['location'].encode('utf8', 'ignore')),
                                  ''.join(item['totalprice'].encode('utf8', 'ignore')),
                                  ''.join(item['unitprice'].encode('utf8', 'ignore')),
                                  ''.join(item['floorlevels'].encode('utf8', 'ignore')),
                                  ''.join(item['housetype'].encode('utf8', 'ignore')),
                                  ''.join(item['constructarea'].encode('utf8', 'ignore')),
                                  ''.join(item['hourse_construction'].encode('utf8', 'ignore')),
                                  ''.join(item['housearea'].encode('utf8', 'ignore')),
                                  ''.join(item['building_types'].encode('utf8', 'ignore')),
                                  ''.join(item['housearea'].encode('utf8', 'ignore')),
                                  ''.join(item['lift_user_ratio'].encode('utf8', 'ignore')),
                                  ''.join(item['propertylimit'].encode('utf8', 'ignore')),
                                  ''.join(item['sale_time'].encode('utf8', 'ignore'))))
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
