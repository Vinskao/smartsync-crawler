# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    title = scrapy.Field()           # 商品標題
    note = scrapy.Field()            # 簡短備註
    price = scrapy.Field()           # 原價
    price_actual = scrapy.Field()    # 實際售價
    qa_text = scrapy.Field()         # 問答內容
    intro_text = scrapy.Field()      # 簡介文字
    product_image = scrapy.Field()   # 主圖片 URL
    spec_image = scrapy.Field()      # 規格圖片 URL
    videolink_text = scrapy.Field()  # 影片連結
    pass
