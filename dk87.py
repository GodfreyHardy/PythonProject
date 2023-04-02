


"""
【静态扫描】
5
1 2 2 1 2 3 4
1 1 1 1 1 1 1
7

5
2 2 2 2 2 5 2 2 2
3 3 3 3 3 1 3 3 3
9
"""
if __name__ == '__main__':
    m = int(input())
    s = input().split(' ')
    ft = [int(x) for x in s]
    s = input().split(' ')
    lt = [int(x) for x in s]
    #贪心策略
    dic = {}
    cost = {}
    for i in range(len(lt)):
        if ft[i] not in dic:
            dic[ft[i]] = 1
        else:
            dic[ft[i]] += 1
        if ft[i] not in cost:
            cost[ft[i]] = lt[i]
    res = 0
    for key in dic:
        res += min(cost[key]*dic[key],m+cost[key])
    print(res)