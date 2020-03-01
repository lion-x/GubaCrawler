# -*- coding: utf-8 -*-
import scrapy
from Guba.items import GubaItem

class GubaSpider(scrapy.Spider):
    name = 'guba'
    allowed_domains = ['guba.sina.com.cn']
    start_urls = ['http://guba.sina.com.cn/?s=bar&name=sh000001']

    def parse(self, response):
        postings = response.xpath('//tr[@class="tr2"]')
        for posting in postings:
            item = GubaItem()
            item['click_number'] = posting.xpath('.//td[1]/span/text()').extract_first()
            item['reply_number'] = posting.xpath('.//td[2]/span/text()').extract_first()
            item['title'] = posting.xpath('.//a[@class=" linkblack f14"]/text()').extract_first()
            item['author'] = posting.xpath('.//div[@class="author"]/a/text()').extract_first()
            item['publish_time'] = posting.xpath('.//td[5]/text()').extract_first()
            yield item
