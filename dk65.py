"""
■ 题目描述
【快速开组建站】
input:
5
5
0 4
1 2
1 3
2 3
2 4
output:
3
input:
5
3
0 3
0 4
1 3
output:
2
"""

import queue
if __name__ == '__main__':
    # 求树的最大深度 层序遍历
    n = int(input())
    m = int(input())
    dic = {}
    sign = [0]*n
    for i in range(m):
        s = input()
        s = s.split(' ')
        k = int(s[0])
        v = int(s[1])
        if k not in dic:
            dic[k] = {}
            dic[k][v] = 1
        else:
            dic[k][v] = 1
    print(dic)
    res = 0
    q = queue.Queue()
    for i in range(n):
        q.put(i)
        level = 1
        while not q.empty():
            top = q.get()
            if top in dic:
                for k in dic[top]:
                    q.put(k)
                level += 1
        res = max(res,level)

    print(res)