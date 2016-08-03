from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from ScrapyTest.items import *
from ScrapyTest.misc.log import *


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["gpai.net"]
    start_urls = [
        "http://www.gpai.net/sf/Search.do?at=376&Page=1"
    ]
    rules = [
        Rule(sle(allow=("/sf/Search.do?at=376&Page=\d{1,3}")), follow=True, callback='parse_item')
    ]



    def parse_item(self, response):
        urls=[];
        sel = Selector(response)
        base_url = get_base_url(response)
        sites=sel.css('.sou-cont2-left .itemlist li')
        for site in sites:
            url=site.css('.sou-cont2-left02 .sou-left02-info1 a').xpath('@href').extract()[0]
            urls.append(url)

         for url in urls:
31              yield Request(url)

        '''
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        sites_even = sel.css('table.tablelist tr.even')
        for site in sites_even:
            item = TencentItem()
            item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
            relative_url = site.css('.l.square a').xpath('@href').extract()[0]
            item['detailLink'] = urljoin_rfc(base_url, relative_url)
            item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
            item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
            item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
            item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
            items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        sites_odd = sel.css('table.tablelist tr.odd')
        for site in sites_odd:
            item = TencentItem()
            item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
            relative_url = site.css('.l.square a').xpath('@href').extract()[0]
            item['detailLink'] = urljoin_rfc(base_url, relative_url)
            item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
            item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
            item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
            item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
            items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        info('parsed ' + str(response))
        return items
        '''

    def _process_request(self, request):
        info('process ' + str(request))
        return request