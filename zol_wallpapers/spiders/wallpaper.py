# -*- coding: utf-8 -*-
import os
import re

from scrapy import Spider, Request

from zol_wallpapers.items import ZolWallpapersItem


class WallpaperSpider(Spider):
    name = 'wallpaper'
    allowed_domains = ['desk.zol.com.cn', 'desk-fd.zol-img.com.cn']
    start_urls = ['http://desk.zol.com.cn']

    img_path = os.path.join(os.getcwd(), 'wallpapers')
    img_list = []

    def start_requests(self):
        try:
            start_urls = 'http://desk.zol.com.cn/1366x768_p4/'
            yield Request(start_urls, callback=self.parse_index, meta={'download_timeout': 3})
        except TimeoutError:
            self.start_requests()

    def parse_index(self, response):
        detail_urls = response.xpath('//li[contains(@class, "photo-list-padding")]/a/@href').extract()
        for url in detail_urls:
            try:
                yield Request(self.start_urls[0] + url, callback=self.parse_detail, meta={'download_timeout': 3})
            except Exception:
                yield Request(self.start_urls[0] + url, callback=self.parse_detail, meta={'download_timeout': 3})
        next = response.xpath('//div[@class="page"]/a[@id="pageNext"]/@href').extract_first()
        try:
            yield Request(self.start_urls[0] + next, callback=self.parse_index, meta={'download_timeout': 3})
        except Exception:
            yield Request(self.start_urls[0] + next, callback=self.parse_index, meta={'download_timeout': 3})

    def parse_detail(self, response):
        pic_url = response.xpath('//div[@id="mouscroll"]/img/@src').extract_first()
        pic_url = re.sub(r'/t_s.*?c5/', '/t_s1366x768c5/', pic_url)
        next_pic = response.xpath('//div[contains(@class, "photo-next")]/a/@href').extract_first()
        item = ZolWallpapersItem()
        item['image_urls'] = [pic_url]
        yield item

        cur_num = response.xpath('//span[@class="current-num"]/text()').extract_first()
        total_num = response.xpath('//div[contains(@class, "wrapper photo-tit")]/h3/span/text()[2]').extract_first()[
                    1:-1]
        if int(cur_num) < int(total_num):
            try:
                yield Request(self.start_urls[0] + next_pic, callback=self.parse_detail, meta={'download_timeout': 3})
            except Exception:
                yield Request(self.start_urls[0] + next_pic, callback=self.parse_detail, meta={'download_timeout': 3})
