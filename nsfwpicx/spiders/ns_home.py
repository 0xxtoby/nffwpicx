import pprint
import re

import scrapy
from scrapy import cmdline
from nsfwpicx.items import NsfwpicxItem
class NsHomeSpider(scrapy.Spider):
    name = 'ns_home'

    def start_requests(self):
        # urls = [
        #     'http://nsfwpicx.com/search/jk/2',
        #     'http://nsfwpicx.com/search/jk/3',
        # ]
        #
        # i=0
        # for url in urls:
        #     i=i+1
        #     yield scrapy.Request(url=url, callback=self.parse,meta={'no':i})



        for i in range(20,30):
            url_a='http://nsfwpicx.com/search/jk/'
            url=url_a+str(i)
            yield scrapy.Request(url=url, callback=self.parse, meta={'no': i})



    def parse(self, response):
        # print(response.body)
        print('==================================================================')
        print('==================================================================')
        print('=============================主界面================================')
        print(response.meta['no'])
        no=response.meta['no']
        print(response.url)
        f=open('html/'+str(response.meta['no'])+'.html','wb')
        f.write(response.body)

        url_list=response.xpath('//*[@id="index-list"]/ul/li/a/@href').extract()
        pprint.pprint(url_list)

        for i in range(len(url_list)):

            yield  scrapy.Request(url=url_list[i],callback=self.url_for,meta={'no':no})


    def url_for(self,response):
        # print(response.body)
        print(response.meta['no'])
        item=NsfwpicxItem()

        id_data=re.split('/',response.url)[-1]
        # print(id_data)
        id=re.split('\.',id_data)[0]



        f=open('html/22.html','wb')
        f.write(response.body)

        jpg_url_list=response.xpath('//*[@id="post"]/article/div[2]/p/figure/a/@href').extract()
        # pprint.pprint(jpg_url_list)
        # pprint.pprint(len(jpg_url_list))

        # print(id)

        item['url_data']=jpg_url_list
        item['len']=len(jpg_url_list)
        item['id']=id
        item['no']=response.meta['no']

        yield item











if __name__ == '__main__':
    cmdline.execute("scrapy crawl ns_home  ".split())

