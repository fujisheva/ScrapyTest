#-*- coding: UTF-8 -*-
import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.http import Request

from ScrapyTest.items import *
#import json
#import urllib2
#from ScrapyTest.misc.log import *


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["gpai.net"]
    start_urls=[]

    for pn in range(1,199):
        url="http://www.gpai.net/sf/Search.do?at=376&Page=%s" % pn
        start_urls.append(url)

    def parse(self,response):
        urls = response.xpath('//*[@class="sou-cont2-left01"]/a/@href').extract()
        for url in urls:
            item_id=url.split('=')[1]
            url_new = 'http://www.gpai.net/sf/' + url
            yield Request(url_new,callback=lambda arg1=response,arg2=item_id:self.parse_item(arg1,arg2))

    def parse_item(self,response,item_id):
        sel = Selector(response)
        item = ScrapytestItem()
        item['itemID']=item_id
        item['title']=sel.css('.DivItemName').xpath('text()').extract()[0]
        item['area'] = sel.css('.xq-right1 > div:nth-child(5) > li:nth-child(1)::text').extract()[0]
        item['method'] = sel.css('.xq-right1 > div:nth-child(5) > li:nth-child(2)::text').extract()[0]
        item['times'] = sel.css('.xq-right1 > div:nth-child(5) > li:nth-child(3)::text').extract()[0]
        item['avPrice'] = sel.css('.xq-right1 > div:nth-child(5) > li:nth-child(4)::text').extract()[0]
        item['bond'] = sel.css('.xq-right1 > div:nth-child(5) > li:nth-child(5)::text').extract()[0]
        item['facility'] = sel.css('.xq-right1 > div:nth-child(5) > li:nth-child(9) > .ellipsis > p::text').extract()[0]
        ajax="http://www.gpai.net/sf/Item_Data.do?Web_Item_ID=%s" % item['itemID']
        yield Request(ajax,callback=lambda arg1=response,arg2=item:self.parse_ajax(arg1,arg2))


    def parse_ajax(self,response,item):
        my_list=response.body_as_unicode()
        item['status']=my_list
        return item
    '''
    def parse_url(self, response):
        urls=[];
        sel = Selector(response)
        base_url = get_base_url(response)
        sites=sel.css('.sou-cont2-left > .itemlist > li')
        for site in sites:
            url=UrlItem()
            url['url']=base_url+site.css('.sou-cont2-left01 > a').xpath('@href').extract()[0]
            urls.append(url)

        return urls
    '''

    def _process_request(self, request):
        info('process ' + str(request))
        return request
