#！/usr/bin/env python
# -*- coding:utf-8 -*-

'''
class Graph(object):

    def __init__(self):
        self.node=[]
        self.connect={}

    def appendNode(self,node):
        self.node.append(node)

    def appendConnect(self,):



if __name__=='__main__':
    graph=Graph()
    node=[1,2,3,4,5]
    for n in node:
        graph.appendNode(n)
'''


class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.

        """

            self.board = board

            self.solve(0)

    def solve(self, index):
        if index == 81:
            return True
        i, j = divmod(index, 9)
        if self.board[i][j] != '.':
            return self.solve(index + 1)
        for c in xrange(1, 10):
            self.board[i][j] = str(c)
            if self.valid() and self.solve(index + 1):
                return True
            self.board[i][j] = '.'
        return False

    def valid(self):
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i, row in enumerate(self.board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))


if __name__'__main__':
    s = Solution(["..9748...", "7........", ".2.1.9...", "..7...24.",
                  ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."])
    print board
