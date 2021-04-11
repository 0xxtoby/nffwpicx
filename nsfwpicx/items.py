# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NsfwpicxItem(scrapy.Item):
    # define the fields for your item here like:
    url_data = scrapy.Field()
    id = scrapy.Field()
    len = scrapy.Field()
    no = scrapy.Field()



