# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZolWallpapersItem(scrapy.Item):
    image_urls = Field()
    # images = Field()
    image_paths = Field()
