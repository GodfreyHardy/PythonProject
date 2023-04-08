

"""
【统一限载货物数最小】
"""

import heapq

def search(goods,k):
    hq = []
    res = -1
    kmax = 0
    for i in range(len(goods)):
        sumitem = 0
        kmax += len(goods[i])
        for j in range(len(goods[i])):
            sumitem += goods[i][j]
        heapq.heappush(hq,[-sumitem,goods[i]])
    if k > kmax:
        k = kmax
    if len(goods) == k:
        top = heapq.heappop(hq)
        return -top[0]

    while 0 < len(hq) < k:
        top = heapq.heappop(hq)
        while len(top[1]) == 1:
            res = max(res, -top[0])
            top = heapq.heappop(hq)
        sumitem = -top[0]
        cursum = 0
        i = 0
        while cursum < sumitem//2:
            cursum += top[1][i]
            i += 1
        if cursum == sumitem//2:
            heapq.heappush(hq, [-sumitem + cursum, top[1][i - 1::]])
            heapq.heappush(hq, [-1 * cursum, top[1][0:i - 1]])
        else:
            cursum -= top[1][i-1]
            heapq.heappush(hq, [-sumitem+cursum, top[1][i - 1::]])
            heapq.heappush(hq, [-1*cursum, top[1][0:i - 1]])
    while len(hq) > 0:
        top = heapq.heappop(hq)
        res = max(res,-top[0])
    return res


if __name__ == '__main__':
    n = int(input())
    s = input().split(' ')
    goods = [int(x) for x in s]
    s = input().split(' ')
    kinds = [int(x) for x in s]
    k = int(input())
    pre = -1
    dry_item = []
    wet_item = []
    drygoods = []
    wetgoods = []
    for i in range(n):
        if i == 0:
            pre = kinds[i]
            if kinds[i] == 0:
                dry_item.append(goods[i])
            elif kinds[i] == 1:
                wet_item.append(goods[i])
        else:
            if kinds[i] != pre:
                pre = kinds[i]
                if kinds[i] == 0:
                    dry_item.append(goods[i])
                    wetgoods.append(wet_item)
                    wet_item = []
                elif kinds[i] == 1:
                    wet_item.append(goods[i])
                    drygoods.append(dry_item)
                    dry_item = []
            else:
                if kinds[i] == 0:
                    dry_item.append(goods[i])
                elif kinds[i] == 1:
                    wet_item.append(goods[i])
    if len(dry_item) > 0:
        drygoods.append(dry_item)
    if len(wet_item) > 0:
        wetgoods.append(wet_item)
    print(drygoods)
    print(wetgoods)
    if k < len(drygoods) or k < len(wetgoods):
        print(-1)
    else:
        drymax = search(drygoods,k)
        wetmax = search(wetgoods,k)
        res = max(drymax,wetmax)
        print(res)
"""
4
3 2 6 3
0 1 1 0
2

6

4
3 2 6 8
0 1 1 1
1

16
"""