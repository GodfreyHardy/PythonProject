"""
■ 题目描述
【城市聚集度】
一张地图上有n个城市，城市和城市之间有且只有一条道路相连：要么直接相连，要么通过其它城市中转相连（可中转一次或多次）。城市与城市之间的道路都不会成环。
当切断通往某个城市 i 的所有道路后，地图上将分为多个连通的城市群，设该城市i的聚集度为DPi（Degree of Polymerization），DPi = max（城市群1的城市个数，城市群2的城市个数，…城市群m 的城市个数）。
请找出地图上DP值最小的城市（即找到城市j，使得DPj = min(DP1,DP2 … DPn))
提示：如果有多个城市都满足条件，这些城市都要找出来（可能存在多个解）
提示：DPi的计算，可以理解为已知一棵树，删除某个节点后；生成的多个子树，求解多个子数节点数的问题。
输入描述：
每个样例：第一行有一个整数N，表示有N个节点。1 <= N <= 1000。
接下来的N-1行每行有两个整数x，y，表示城市x与城市y连接。1 <= x,  y <= N
输出描述：
输出城市的编号。如果有多个，按照编号升序输出。
示例1   输入输出示例仅供调试，后台判题数据一般不包含示例
输入
5
1 2
2 3
3 4
4 5
输出
3
"""
import copy
import queue

if __name__ == '__main__':
    n = int(input())
    graph = {}
    graphchild = {}
    node = {}
    for i in range(n - 1):
        s = input()
        s = s.split(' ')
        p = int(s[0])
        c = int(s[1])
        if p not in graph:
            graph[p] = []
        graph[p].append(c)
        if c not in graphchild:
            graphchild[c] = []
        graphchild[c].append(p)
        node[p] = 1
        node[c] = 1
    dic = {}
    minnum = 10000
    for cur in node:
        sign = copy.deepcopy(node)
        sign[cur] = 0
        q = queue.Queue()
        maxcount = -1
        for item in node:
            if item != cur and sign[item] == 1:
                q.put(item)
                sign[item] = 0
                nodecount = 1
                while not q.empty():
                    top = q.get()
                    if top in graph:
                        for i in range(len(graph[top])):
                            if graph[top][i] != cur and sign[graph[top][i]] == 1:
                                q.put(graph[top][i])
                                nodecount += 1
                                sign[graph[top][i]] = 0
                    if top in graphchild:
                        for i in range(len(graphchild[top])):
                            if graphchild[top][i] != cur and sign[graphchild[top][i]] == 1:
                                q.put(graphchild[top][i])
                                nodecount += 1
                                sign[graphchild[top][i]] = 0
                maxcount = max(maxcount, nodecount)
        dic[cur] = maxcount
        minnum = min(minnum, maxcount)
    # 排序
    a = sorted(dic.items(), key=lambda x: (x[1], x[0]))
    res = ""
    print(a)
    print(minnum)
    for item in a:
        if int(item[0]) == minnum:
            res += str(item[1]) + ' '
    res = res[0:len(res) - 1]
    print(res)
