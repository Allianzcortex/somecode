#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import defaultdict
from operator import itemgetter
# 它如何用 Python 的并查集来进行优化呢？

class Graph(object):

    def __init__(self):
        self.nodes=set()
        self.end_node=dict()
        self.distances={}

    def add_node(self,value):
        self.nodes.add(value)
        #self.end_node[value]=None # 再看 defaultdict 的使用

    def add_edges(self,from_node,to_node,value):
        self.distances[(from_node,to_node)]=value


    def kruskal(self):
        MKT={} # 维护一个集合
        distances=self.distances
        end_node=self.end_node
        print distances
        print end_node
        for item,value in sorted(distances.items(),key=itemgetter(1)): # 感觉顺序不应该是这个啊

            origin,destination=item
            try:
                s1=end_node[origin]
                s2=end_node[destination]
                if s1==s2:
                    continue

            except KeyError:
                pass
            

            print origin,destination
            MKT.update({(origin,destination):value})
            end_node.update({origin:None})
            end_node.update({destination:None})
            target=sorted(end_node.keys())[-1]
            for n in end_node.keys():
                end_node[n]=target
            print end_node
        print MKT

if __name__=='__main__':
    graph=Graph()
    for node in ['A','B','C','D','E','F','G']:
        graph.add_node(node)
    graph.add_edges('A','B',5)
    graph.add_edges('B','D',2)
    graph.add_edges('D','F',4)
    graph.add_edges('F','E',4)
    graph.add_edges('E','C',5)
    graph.add_edges('C','A',6)
    graph.add_edges('A','D',4)
    graph.add_edges('B','C',1)
    graph.add_edges('C','F',3)

    graph.kruskal()






