# -*- coding: utf-8 -*-
import scrapy


class ConductSpider(scrapy.Spider):
    name = 'conduct'
    allowed_domains = ['www.drthawip.com/criminalcode/1']
    start_urls = ['http://www.drthawip.com/criminalcode/1/']

    def parse(self, response):
        pass
