#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import defaultdict, deque


class Graph(object):

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self,from_node, to_node, value):
        self.edges[from_node].append(to_node)
        #self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = value

    def dijkstra(self, initial):
        visited = {initial: 0}
        paths = {}

        nodes = self.nodes

        print nodes,self.edges

        while nodes:
            min_node = None
            for node in nodes: # ……for none in nodes
                if node in visited:
                    if min_node == None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for to in self.edges[min_node]:
                
                weight = self.distances[(min_node, to)] + current_weight
                
                if to not in visited or weight < visited[to]:
                    visited[to] = weight
                    paths[to] = min_node



        return visited, paths

    def shortest_path(self, origin, destination):
        final_path = deque()
        visited, paths = self.dijkstra(origin)

        print 'visited{},paths{}'.format(visited,paths)

        temp = paths[destination]
        while temp is not origin:
            final_path.appendleft(temp)
            temp = paths[temp]
        final_path.appendleft(origin)
        final_path.append(destination)

        return visited[destination], final_path

if __name__=='__main__':
    graph=Graph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 30)
    graph.add_edge('B', 'E', 50)
    graph.add_edge('D', 'E', 30)
    graph.add_edge('E', 'F', 5)
    graph.add_edge('F', 'G', 2)

    print graph.shortest_path('A','D')

    # 下面实现 Prim 和 Kruskal 算法啊