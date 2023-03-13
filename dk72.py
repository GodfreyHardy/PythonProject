



#【平均数】
if __name__ == '__main__':
    s = input().split(' ')
    lt = []
    for i in range(len(s)):
        lt.append(int(s[i]))
    min1 = 2147483647
    res = 0
    for k in range(-255,256,1):
        sumitem = 0
        for i in range(len(lt)):
            item = lt[i]+k
            if lt[i]+k < 0:
                item = 0
            elif lt[i]+k > 255:
                item = 255
            sumitem += item
        average = sumitem/len(lt)
        print(abs(average-128.0))
        if abs(average-128.0) < min1:
            min1 = abs(average-128.0)
            res = k
    print(res)