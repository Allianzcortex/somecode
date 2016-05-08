#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
s=socket.socket()
s.connect(('www.baidu.com',80)) # 程序阻塞在了connect的调用上，称为阻塞式的
print 'get the {}'.format(s.getpeername())

# 下面是非阻塞方式的
s = socket.socket()
s.setblocking(0) # 设置为非阻塞

try:
    s.connect(('www.google.com', 80))
except socket.error as e:
    print(str(e))
    i = 0
    while True:
        try:
            print("We are connected to %s:%d" % s.getpeername())
            break
        except:
            print("Let's do some math while waiting: %d" % i)
            i += 1
else:
    print("We are connected to %s:%d" % s.getpeername())

# 阻塞是等到一个函数返回值的时候
# 非阻塞是调用之后立即返回，等待其他的函数来给自己返回信息

# 下面是关于同步和异步

# 同步的方式比如自己写的爬虫 r=requests.get()
# 之后对 r.content 来进行处理
# 所以说同步一般都是阻塞的

# 下面是关于异步的知识

# 一个示例代码：
# 基于 twisted 实现
while server.running:
    deferred = server.receive()
    deferred.addCallback(on_request)

def on_request(request):
    deferred = handle(request)
    deferred.addCallback(on_response)

def on_response(response):
    server.send(response)

# 为了实现异步，receiver() 和 handle() 都是非阻塞的
#在 Twisted 中非阻塞的函数会立即返回一个 Deferred 对象，通过给 Deferred 对象添加
# 回调函数，我们可以实现在这件事情真正完成之后，执行回调函数中定义的接下来要做的事儿。

# 一些异步框架提供了同步的借口来写

# 并发和并行

'''
并行概念主要在处理端。5个窗口，说明同一时间可以处理5个任务
这就要求需要多个 CPU 来做
用单 CPU 实现的技术是 时分复用

'''

只有一个线程，用阻塞调用的方式是无法实现并发的，因此
用非阻塞方式

wdict = {}
for word in words:
    try:
        wdict[word] += 1
    except KeyError:
        wdict[word] = 1

from collections import defaultdict

wdict = defaultdict(int)

for word in words:
    wdict[word] += 1
