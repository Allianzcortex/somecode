#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
from random import randint
import time
from base64 import b64decode,b64encode


class Spider(object):

    
    def __init__(self):
        self.count=0

    def crawl_baidu(self): # 到第 6300 

        count = 990
        for index in xrange(5857, 9999):
            # http://music.baidu.com/songlist/6416
            print index
            url = 'http://music.baidu.com/songlist/' + str(index)
            print url

            r = requests.get(url)
            if r.content.find('404') is not -1:
                continue
            title=re.findall('<a class="list-micon icon-play" data-action="play" title="播放(.*?)"',r.content)
            content = re.findall('class="song-title " style=.*?<a href="(.*?)"',r.content)
            if len(content) < 5:
                continue

            count += 1
            # res=''.join(content)

            with open('data.txt', 'a') as f:
                for i,song_title in enumerate(title):
                    try:
                        song_url=content[i]
                    except IndexError: # 有些无法完全匹配
                        continue
                    t=requests.get('http://music.baidu.com/'+song_url)
                    rating=re.findall('<span class="num">(.*?)</span>',t.content)
                    try:
                        rating=int(''.join(rating).replace(',',''))
                    except ValueError:
                        rating=1 # 表示刚上架

                    if rating<500:
                            rating=1
                    elif 500<=rating<=1000:
                            rating=2
                    elif 1000<=rating<=2000:
                            rating=3
                    elif 2000<=rating<=3000:
                            rating=4
                    elif rating>=3000:
                            rating=5

                    f.writelines(str(count) + ' ' + song_title + ' '+'http://music.baidu.com'+song_url+' ' + str(rating) + '\n')
                f.writelines('\n')
                #time.sleep(3)
        global all_count
        all_count=count

    def crawl_kuwo(self):

        count = 23282
        for index in xrange(39755, 100000):
            # http://music.baidu.com/songlist/6416
            print index
            url = 'http://www.kuwo.cn/album/' + str(index)
            print url

            r = requests.get(url)
            #print r.content
            if r.content.find('对不起') is not -1:
                continue
            content = re.findall(
                '<a href="http://www.kuwo.cn/yinyue/(.*?)" title="(.*?)" target="_blank">', r.content)
            if len(content) < 5:
                continue

            count += 1
            # res=''.join(content)

            with open('licicunzhao.txt', 'a') as f:
                for url,target in content:
                    print target
                    f.writelines(str(count) + ' ' + target + ' '+'www.kuwo.yinyue/'+url+\
                                 ' ' + str(randint(1, 5)) + '\n')
                f.writelines('\n')
            time.sleep(1)




    def dealfile(self):
        
        
        with open('data.txt', 'r') as input:
            for line in input:
                #print line
                #print type(line)
                
                line=list(line.split()) # 这里不应该犯这种错误呀，很简单的一种
                print line
                if not line:
                    continue
                #print line
                UserID = line.pop(0)
                rating = line.pop()
                title = ''.join(line)
                new_title = b64encode(title)

                with open('temp.txt', 'a') as output:
                    output.writelines(UserID + ' ' +new_title + ' '+ rating + '\n')
                
        

if __name__ == '__main__':

    s = Spider()
    #s.crawl_baidu()
    s.crawl_kuwo()
    #s.dealfile()