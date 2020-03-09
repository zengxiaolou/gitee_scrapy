# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import urllib

from ..items import GiteeItem, GiteeItemLoader


class GiteeRedisSpider(RedisCrawlSpider):
    name = 'gitee_redis'
    allowed_domains = ['gitee.com']
    redis_key = 'gitee_redis:start_urls'

    rules = (
            Rule(LinkExtractor(allow=r"/explore/.*-.*"), callback='parse_item', follow=False),
        )

    def parse_item(self, response):
        li_list = response.css(".explore-projects__detail-list .explore-repo__list .item")
        category = response.css(
            ".explore-projects__detail-list .explore-project__selection-container .section::text").extract_first()
        for li in li_list:
            item_loader = GiteeItemLoader(item=GiteeItem(), selector=li)
            item_loader.add_value('category', category)
            item_loader.add_css('avatar', '.avatar img::attr(src)')
            item_loader.add_css('title', '.title::text')
            item_loader.add_css('gvp', '.js-popup-default::attr(title)')
            item_loader.add_css('lang', '.lang-label::text')
            item_loader.add_css('label', '.project-meta a:nth-child(2)::text')
            item_loader.add_css('watch', '.explore-project__meta-social a:nth-child(1) span::text')
            item_loader.add_css('star', '.explore-project__meta-social a:nth-child(2) span::text')
            item_loader.add_css('fork', '.explore-project__meta-social a:nth-child(3) span::text')
            item_loader.add_css('desc', '.project-desc::text')
            item_loader.add_css('latest', '.project-latest span:nth-child(1)::attr(title)')
            item = item_loader.load_item()
            yield item
        next_url = response.css('#git-discover-page a[rel="next"]::attr(href)').extract_first()
        if next_url:
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_item,
            )