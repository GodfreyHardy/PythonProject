







if __name__ == '__main__':
    m = int(input())
    s = input().split(' ')
    file = [int(x) for x in s]
    s = input().split(' ')
    size = [int(x) for x in s]
    dic = {}
    cost = {}
    for i in range(len(file)):
        if file[i] not in dic:
            dic[file[i]] = 1
        else:
            dic[file[i]] += 1
        if file[i] not in cost:
            cost[file[i]] = size[i]
    res = 0
    for key in dic:
        pay1 = cost[key]*dic[key]
        pay2 = cost[key]+m
        res += min(pay1,pay2)
    print(res)
"""
5
2 2 2 2 2 5 2 2 2
3 3 3 3 3 1 3 3 3
"""