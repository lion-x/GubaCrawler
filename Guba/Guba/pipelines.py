# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.exporters import CsvItemExporter
# import json
from openpyxl import Workbook


# class GubaPipeline(object):
#     def __init__(self):
#         self.file = open('Guba/data/postings.csv', 'w')
#
#
#     def process_item(self, item, spider):
#         content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#         self.file.write(content)
#         return item
#
#
#     def close_spider(self, spider):
#         self.file.close()

# class GubaPipeline(object):
#     def open_spider(self, spider):
#         self.file = open('Guba/data/postings.csv', 'wb')
#         self.exporter = CsvItemExporter(self.file,
#                                         fields_to_export=["click_number", "reply_number",
#                                                           "title", "author", "publish_time"])
#         self.exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         # content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#         # self.file.write(content)
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()

class GubaPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['点击', '回复', '标题', '作者', '发表时间'])


    def process_item(self, item, spider):
        line = [item['click_number'], item['reply_number'], item['title'], item['author'], item['publish_time']]
        self.ws.append(line)
        return item


    def close_spider(self, spider):
        self.wb.save('Guba/data/postings.xlsx')
