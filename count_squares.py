import queue

if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    m = int(s[1])
    c = int(s[2])
    target = int(s[3])
    lt = [[0]*m for i in range(n)]
    for i in range(n):
        s = input()
        s = s.split(' ')
        for j in range(m):
            lt[i][j] = int(s[j])
    print(lt)
    row = queue.Queue()
    col = queue.Queue()
    sumtmp = 0
    for i in range(c):
        sumr = 0
        sumc = 0
        for j in range(c):
            sumr += lt[i][j]
            sumtmp += lt[i][j]
            sumc += lt[j][i]
        row.put(sumr)
        col.put(sumc)
    res = 0
    if sumtmp>=target:
        res += 1
    for i in range(c-1,n):
        if i >= c:
            sumtmp -= row.get()
            sumrow = 0
            for k in range(0,c):
                sumrow +=lt[i][k]
                top = col.get()
                top += lt[i][k]
                top -= lt[i-c][k]
                col.put(top)
            row.put(sumrow)
            sumtmp += sumrow
            if sumtmp>=target:
                res += 1
        col2 = queue.Queue()
        lqueue = []
        while not col.empty():
            item = col.get()
            lqueue.append(item)
            col2.put(item)
        for i3 in range(len(lqueue)):
            col.put(lqueue[i3])
        sumtmp2 = sumtmp
        for j in range(c,m):
            sumtmp2 -= col2.get()
            sumcol = 0
            for i2 in range(i+1-c,i+1):
                sumcol += lt[i2][j]
            col2.put(sumcol)
            sumtmp2 += sumcol
            if sumtmp2 >= target:
                res += 1
    print(res)
