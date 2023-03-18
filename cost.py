

def buy_goods(n, x, y, items):
    items.sort(key=lambda x: x[1])  # 按照折从小到大排序
    # print(items)
    count = 0  # 已购买的商品数量
    cost = 0  # 已花费的总金额
    for item in items:
        if y > 0:  # 如果还有折扣券，就使用一张折扣券购买该物品
            cost += item[1]
            y -= 1
            x -= item[1]
            item[0] = 9999
            item[1] = 9999
            count += 1
        # elif x >= item[0]:  # 否则如果钱够购买该物品，就用现金购买
        #     cost += item[0]
        #     x -= item[0]
        else:  # 如果钱不够购买该物品，就退出循环
            break
    # print(items)
    # print(cost)
    items.sort(key=lambda x: x[0])
    # print(items)
    for item in items:
        if item[0]==9999:
            break
        if x >= item[0]:
            cost += item[0]
            x -= item[0]
            count += 1
        else:
            break
    return count, cost
"""
3 5 1
4 3
3 1
6 5

2 5

3 5 2
4 3
3 1
6 5
2 4 
"""

if __name__ == '__main__':
    s = input().split(' ')
    n = int(s[0])
    x = int(s[1])
    y = int(s[2])
    lt = [[0]*2 for _ in range(n)]
    for i in range(n):
        s = input().split(' ')
        lt[i][0] = int(s[0])
        lt[i][1] = int(s[1])
    # print(buy_goods(n,x,y,lt))
    k1,k2 = buy_goods(n,x,y,lt)
    print(str(k1)+' '+str(k2))