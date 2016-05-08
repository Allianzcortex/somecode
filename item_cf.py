#！/usr/bin/env python
# -*- coding:utf-8 -*-

import math
from operator import itemgetter

class ItemCF(object):

    def __init__(self):
        self.trainset = self.load_file('ml-100k/u1.base')
        self.testset=self.load_file('ml-100k/u1.test')
        self.cal_similarity()

    def load_file(self, filename):
        w = dict()
        with open(filename, r) as f:
            for line in f:
                UserID, MovieID, Rating, TimeStamp = line.split()
                w.setdefault(UserID, {}).update({MovieID: Rating})
        return w  # 建立用户-物品倒排表

    def cal_similarity(self):
        # 计算相似度
        trainset = self.trainset
        # 这里如果用 []*x 的矩阵来计算，恐怕不好掌握长度
        # N(i) 表示的是喜欢物品i的用户数
        # C[i][j] 表示的是喜欢物品i的同时喜欢物品j的用户数
        counter=dict()
        simMatrix=dict()

        for user,related_items in trainset.items():
            for item in related_items.keys():
                counter[item]+=1
                
                simItems=simMatrix.setdefault(item,{})

                for j in related_items.keys():
                    if not item==j:
                        simItems.setdefault(j,0)
                        simItems[j]+=1

        for i,item in simMatrix:
            for j in item.keys():
                simMatrix[i][j]/=math.sqrt(counter[i]*counter[j])
        self.simMatrix=simMatrix

    def cal_recommend(self):
        simMatrix=self.simMatrix
        trainset=self.trainset
        rank=dict()

        for user in trainset:
            items=trainset.get(user)

            for i,rating in items:

                simitems=simMatrix.get(i)

                for j,simIJ in sorted(simitems.items(),key=itemgetter(1),reverse=True)[:k]:
                    if not j in items:
                        rank.setdefault(j,0)
                        rank[j]+=simIJ*rating

                # 下面是对用户的推荐进行生成：
                res=sorted(rank.items(),key=itemgetter(1),reverse=True)[:N]
                self.recommend_result[user]=res

        # 最后的结果是 self.recommend_result

    def cal_recall(self):
        pass

    def cal_coverage(self):

        hit,origin=0,0

        for user in self.testset:
            testitem=self.testset.get(user)
            recomitem=self.recommend_result.get(user)
            for item in recomitem:
                if item in testitem:
                    hit+=1
            origin+=len(testitem)

        return hit/origin



