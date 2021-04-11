# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import pprint

import requests
from itemadapter import ItemAdapter


class NsfwpicxPipeline:
    def process_item(self, item, spider):
        print('data:',item['url_data'])
        dir_name=str(item['id'])+' '+str(item['len'])+'P'
        print('============================================')
        print('=================='+dir_name+'=========================')

        home='Z:\\py\\data\\nsfwpicx\\jk\\'
        dir=home+dir_name
        if not os.path.exists(dir):  # 判断文件夹是否存在
            os.mkdir(dir)

            i = 0
            for url in item['url_data']:
                i = i + 1
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'
                }

                r = requests.get(url, headers=headers).content
                f = open(dir + '\\' + str(i) + '.jpg', 'wb')
                f.write(r)
                print('保存成功：' + dir_name + '\\' + str(i) + '.jpg')

                print('====================================================')
                print('========' + dir_name + '====' + str(item['len']) + '\\' + str(i) + '====' + str(
                    item['no']) + '===============')



        elif len(os.listdir(dir))!=item['len']:
            i = 0
            for url in item['url_data']:
                i = i + 1
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'
                }

                r = requests.get(url, headers=headers).content
                f = open(dir + '\\' + str(i) + '.jpg', 'wb')
                f.write(r)
                print('保存成功：' + dir_name + '\\' + str(i) + '.jpg')

                print('==========文件已存在未满===='+str(len(os.listdir(dir)))+'================================')
                print('========' + dir_name + '====' + str(item['len']) + '\\' + str(i) + '====' + str(
                    item['no']) + '===============')

        else:
            print('文件已存在')



        return item
