import scrapy
import json
import re
from crawler.items import CrawlerItem

class SmartsyncSpider(scrapy.Spider):
    name = 'smartsync_spider'
    allowed_domains = ['jarvis.com.tw']
    start_urls = ['https://www.jarvis.com.tw/aqara智能居家/']

    def parse(self, response):
        # 提取商品列表的 URL
        product_urls = response.css('.ty-grid-list__item a::attr(href)').getall()

        for product_url in product_urls:
            yield response.follow(product_url, callback=self.parse_product)

        # 提取下一頁的 URL
        next_page = response.css('link[rel="next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        item = CrawlerItem()

        item['title'] = response.css('h1.ty-mainbox-title::text').get()
        item['note'] = response.css('.ty-product-feature-list__item::text').getall()
        item['price'] = response.css('.ty-price-num::text').get()
        item['price_actual'] = response.css('.ty-price-num.actual::text').get()
        item['qa_text'] = response.css('.ty-qa__item-text::text').getall()
        item['intro_text'] = response.css('.ty-product-feature-list__description::text').getall()
        item['product_image'] = response.css('.ty-product-feature-list__image img::attr(src)').get()
        item['spec_image'] = response.css('.ty-product-spec-list__image img::attr(src)').get()
        item['videolink_text'] = response.css('.ty-product-video iframe::attr(src)').get()

        yield item