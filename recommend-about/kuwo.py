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

                        '''
                        酷狗抓取的思路应该没错
                        用 r=requests.post('http://sdn.kugou.com/link.aspx',data={'id':12116,'url':'','t':0.0023})
>>> print r.content
{"status":0,"error_code":20019,"data":""}
                        用 fiddler 来抓包
                        '''
            # res=''.join(content)


if __name__ == '__main__':
    spider = Spider()
    spider.crawl_kugo()

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-file /home/hadoop/mapper.py    -mapper /home/hadoop/mapper.py \
-file /home/hadoop/reducer.py   -reducer /home/hadoop/reducer.py \
-input /user/hadoop/* -output /user/hadoop/

hadoop jar hadoop-streaming-2.5.2.jar \
    -input myInputDirs \
    -output myOutputDir \
    -mapper myPythonScript.py \
    -reducer /usr/bin/wc \
    -file myPythonScript.py \
    -file myDictionary.txt

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-input /user/hadoop/* \
-output /user/hadoop/temp1 \
-mapper /home/hadoop/mapper.py \
-reducer /home/hadoop/reducer.py


# 下面的是最终可以执行的方法
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-input /user/hadoop/* -output /user/hadoop/temp1 -mapper /home/hadoop/mapper.py \
-reducer /home/hadoop/reducer.py


yue_chinese_song
europe_song
japan_song
dj_song
traditional_song
electric_song
mental_song
lyric_song
pure_song
grand_song
chinese_song
