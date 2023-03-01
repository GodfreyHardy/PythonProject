"""
■ 题目描述
【开心消消乐】
input:
3 3
1 0 1
0 1 0
1 0 1
output:
1
input:
4 4
1 1 0 0
0 0 0 1
0 0 1 1
1 1 1 1
output:
2
"""
import queue
if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    m = int(s[1])
    lt = []
    sign = [[0]*m for _ in range(n)]
    for i in range(n):
        s = input()
        s = s.split(' ')
        item = []
        item.extend(s)
        lt.append(item)
    q = queue.Queue()
    res = 0
    for i in range(n):
        for j in range(m):
            if lt[i][j]=='1' and sign[i][j]==0:
                q.put(str(i)+'#'+str(j))
                while not q.empty():
                    top = q.get()
                    top = top.split('#')
                    row = int(top[0])
                    col = int(top[1])
                    if row-1>=0 and sign[row-1][col]==0 and lt[row-1][col]=='1':
                        q.put(str(row-1)+'#'+str(col))
                        sign[row-1][col] = 1
                    if row + 1 < n and sign[row + 1][col] == 0 and lt[row + 1][col]=='1':
                        q.put(str(row + 1) + '#' + str(col))
                        sign[row + 1][col] = 1
                    if col - 1 >= 0 and sign[row][col-1] == 0 and lt[row][col-1]=='1':
                        q.put(str(row) + '#' + str(col-1))
                        sign[row][col-1] = 1
                    if col + 1 < m  and sign[row][col + 1] == 0 and lt[row][col+1]=='1':
                        q.put(str(row) + '#' + str(col+1))
                        sign[row][col+1] = 1
                    if row - 1 >= 0 and col - 1 >= 0 and sign[row - 1][col-1] == 0 and lt[row - 1][col-1]=='1':
                        q.put(str(row - 1) + '#' + str(col-1))
                        sign[row - 1][col-1] = 1
                    if row - 1 >= 0 and col + 1 < m  and sign[row - 1][col + 1] == 0 and lt[row - 1][col+1]=='1':
                        q.put(str(row - 1) + '#' + str(col+1))
                        sign[row - 1][col+1] = 1
                    if row + 1 < n and col - 1 >= 0 and sign[row + 1 ][col - 1] == 0 and lt[row + 1][col-1]=='1':
                        q.put(str(row + 1) + '#' + str(col-1))
                        sign[row + 1][col-1] = 1
                    if row + 1 < n and col + 1 < m and sign[row + 1][col + 1] == 0 and lt[row + 1][col+1]=='1':
                        q.put(str(row + 1) + '#' + str(col+1))
                        sign[row + 1][col+1] = 1
                res += 1
    print(res)


