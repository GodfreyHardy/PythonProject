"""
■ 题目描述
【计算快递主站点】
快递业务范围有N个站点，A站点与B站点可以中转快递，则认为A-B站可达，如果A-B可达，B-C可达，则A-C可达。
现在给N个站点编号0、1、…n-1，用s[i][j]表示i-j是否可达，s[i][j]=1表示i-j可达，s[i][j]=0表示i-j不可达。
现用二维数组给定N个站点的可达关系，请计算至少选择从几个主站点出发，才能可达所有站点（覆盖所有站点业务）。
说明：s[i][j]与s[j][i]取值相同。
输入描述
第一行输入为N，N表示站点个数。
之后N行表示站点之间的可达关系，第i行第j个数值表示编号为i和j之间是否可达。
输出描述
输出站点个数，表示至少需要多少个主站点。
补充说明
1 < N < 10000
"""
"""
3
0 1 1
1 0 0
1 0 0
"""
# 连通图个数计算

import queue

if __name__ == '__main__':
    n = int(input())
    lt = [[0] * n for _ in range(n)]
    for i in range(n):
        s = input().split(' ')
        for j in range(n):
            lt[i][j] = int(s[j])
    q = queue.Queue()
    sign = [0]*n
    count = 0
    for i in range(n):
        if sign[i] == 0:
            sign[i] = 1
            q.put(i)
            while not q.empty():
                top = q.get()
                for j in range(n):
                    if j != top and lt[top][j] == 1 and sign[j] == 0:
                        sign[j] = 1
                        q.put(j)
            count += 1
    print(count)

















