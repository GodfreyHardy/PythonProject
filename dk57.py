"""
■ 题目描述
网络信号经过传递会逐层衰减，且遇到阻隔物无法直接穿透，在此情况下需要计算某个位置的网络信号值。
注意:网络信号可以绕过阻隔物。
array[m][n] 的二维数组代表网格地图，
array[i][j] = 0代表i行j列是空旷位置;
array[i][j] = x(x为正整数)代表i行j列是信号源，信号强度是x;
array[i][j] = -1代表i行j列是阻隔物。
信号源只有1个，阻隔物可能有0个或多个
网络信号衰减是上下左右相邻的网格衰减1
现要求输出对应位置的网络信号值。
"""


import queue
if __name__ == '__main__':
    s = input()
    dic = {}
    q = queue.Queue()
    lt = []
    while len(s) > 0:
        s = s.split(' ')
        item = []
        for i in range(len(s)):
            item.append(int(s[i]))
        lt.append(item)
        s = input()
    n = len(lt)
    m = len(lt[0])
    si = 0
    sj = 0
    ti = 0
    tj = 0
    for i in range(n):
        for j in range(m):
            if lt[i][j] > 0:
                si = i
                sj = j
    q.put(str(si)+'#'+str(sj))
    dic[str(si)+'#'+str(sj)] = lt[si][sj]
    while not q.empty():
        top = q.get()
        val = dic[top]
        top = top.split('#')
        row = int(top[0])
        col = int(top[1])

        if row-1>=0 and lt[row-1][col]!=-1:
            k = str(row-1)+'#'+str(col)
            if k not in dic:
                q.put(k)
                dic[k] = val - 1
        if row + 1 < n and lt[row + 1][col] != -1:
            k = str(row + 1) + '#' + str(col)
            if k not in dic:
                q.put(k)
                dic[k] = val - 1
        if col - 1 >= 0 and lt[row][col-1] != -1:
            k = str(row) + '#' + str(col-1)
            if k not in dic:
                q.put(k)
                dic[k] = val - 1
        if col + 1 < m and lt[row][col+1] != -1:
            k = str(row) + '#' + str(col+1)
            if k not in dic:
                q.put(k)
                dic[k] = val - 1
    print(dic)
    k = str(ti)+'#'+str(tj)
    print(dic[k])
"""
0 0 -1
0 10 0
0 0 -1
"""




















