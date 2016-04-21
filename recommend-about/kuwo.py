#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
from random import randint
import time
from base64 import b64decode


class Spider(object):

    def __init__(self):
        pass

    def crawl_kugo(self):

        count = 0
        for index in xrange(1, 80):
            # http://music.baidu.com/songlist/6416
            print index
            url = 'http://www.kugou.com/yy/category/special/1-' + \
                str(index) + '.html'
            print url

            r = requests.get(url)
            # print r.content
            if r.content.find('暂无数据') is not -1:
                continue
            count+=1
            page_number = re.findall(
                '<a  id="page_\d+" href = "(.*?)" >', r.content)
            page_number.append(url)
            for page in page_number:
                t=requests.get(page)
                content = re.findall(
                    '<a title=".*?" href="(.*?)>', t.content)
                for album in content:
                    s=requests.get(album)
                    song_all=re.findall('<li><a title="(.*?) hidefocus="true"',s.content)
                    with open('temp.txt','a') as output:
                        for song_title in song_all:
                            print song_title
                            output.writelines(str(count) + ' '+song_title+' '+randint(1,5)+'\n')
                        output.writelines('\n')
            # res=''.join(content)


if __name__ == '__main__':
    spider = Spider()
    spider.crawl_kugo()
