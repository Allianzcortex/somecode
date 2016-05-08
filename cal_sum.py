#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
可以优化的部分包括：

1. money 可以提前运算，因为是一个固定值
2. 在计算的时候，以 bottle 为例，先用 bottle%=2,之后再对 bottle进行+temp

'''


def cal1():
    money = 10
    bottle, cap, count = 0, 0, 0

    # bottle 空瓶 cap 盖子
    while money >= 2 or bottle >= 2 or cap >= 4:
        if money > 0:
            temp = money / 2
            cap += temp
            count += temp
            bottle += temp
            money %= 2

        if bottle >= 2:
            temp = bottle / 2
            bottle %= 2
            count += temp
            cap += temp
            bottle += temp

        if cap >= 4:
            temp = cap / 4
            cap %= 4
            count += temp
            cap += temp
            bottle += temp

        print 'money:{} bottle {} cap {} count {}'.format(money, bottle, cap, count)
    print count


def cal2():
    money = 10

    print dfs(0, money / 2, 0, 0)


def dfs(count, wine, bottle, cap):
    if wine == 0:
        return count
    count += wine
    bottle += wine
    cap += wine
    wine = 0

    wine += bottle / 2
    wine += cap / 4

    bottle %= 2
    cap %= 4

    return dfs(count, wine, bottle, cap)


def cal3():

#在能够向老板借东西的情况下，得到最优解

#1. 现在有一个空瓶，向老板借一个酒瓶；喝完之后换回去，消耗一个空瓶，得到一个酒+一个盖子
#2. 现在有2个盖子，向老板借2个盖子，换一瓶酒，有一瓶酒+一个空瓶+一个盖子；对一个空瓶，使用上面的操作，得到
#2个酒+2个盖子，再还回去；2个盖子换两次酒喝



    money = 10
    count, bottle, cap, wine = 0, 0, 0, 5
    while True:
        
        count += wine
        bottle += wine
        cap += wine
        wine = 0

        if bottle >= 1:
            # 显然不会用2个空瓶去换啊
            count += bottle
            cap += bottle
            bottle = 0

        if cap >= 2:
            count += (cap / 2)*2 # 自己在想什么……思路要清晰呀。换两次酒喝，要*2啊
            cap %= 2

        if wine == 0 and bottle < 1 and cap < 2:
            break
    print count

if __name__ == '__main__':
    cal1()
    cal2()
    cal3()
