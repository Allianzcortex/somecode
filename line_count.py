#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

def line_count():
    dir_path = '/home/hzcortex/projects/recommend-about/cortexForum'
    exclude = ['.git', '.idea', 'ven', 'migrations', 'static']
    exlude_files = ['base.txt']
    count = 0
    for root, dirs, files in os.walk(dir_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in files:
            if f.endswith('.pyc') or f in exlude_files:
                continue
            print f
            # absolute path
            count += sum([1 for line in open(os.path.join(root, f))])

    print count

if __name__ == '__main__':
    line_count()
