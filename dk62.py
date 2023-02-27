"""
■ 题目描述
【狼羊过河】
input:
5 3 3
output:
3
"""

if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])  # 羊的数目
    m = int(s[1])  # 狼的数目
    k = int(s[2])  # 船的载量
    if n <= m:
        print('0')
    elif n == m + 1:
        if k < n + m:
            print('0')
    else:
        row = n + 1
        col = m + 1
        lt = [[-1] * col for _ in range(row)]  # 对岸的羊狼数量组(羊,狼)
        lt[0][0] = 0
        for i in range(1, row):
            if n - i > m:
                if i % k != 0:
                    lt[i][0] = i // k + 1
                else:
                    lt[i][0] = i // k
        for i in range(1, col):
            if i % k != 0:
                lt[0][i] = i // k + 1
            else:
                lt[0][i] = i // k
        for i in range(1, row):  # 羊的数量
            for j in range(1, col):  # 狼的数量
                if i > j:
                    min1 = 200000000
                    for item in range(1, k + 1):  # 一次运载数量
                        for t in range(0, item + 1):  # 一次运载羊的数量
                            # (t,item-t) (i,j)
                            if i >= t and j >= item - t :
                                if i-t > j-item+t:
                                    if n - i > m - j >= 0 or (m-j>=0 and n-i==0):
                                        if n-i+t > m-j+item-t >=0 or(m-j+item-t>=0 and n-i+t==0):
                                            if lt[i - t][j - item + t]>=0:
                                                min1 = min(min1, lt[i - t][j - item + t])
                                elif i-t == 0:
                                    if j-item+t == 0:
                                        if n - i > m - j >= 0 or (m - j >= 0 and n - i == 0):
                                            if lt[i - t][j - item + t] >= 0:
                                                min1 = min(min1, lt[i - t][j - item + t])
                                    elif j-item+t > 0:
                                        if n - i > m - j >= 0 or (m - j >= 0 and n - i == 0):
                                            if lt[i - t][j - item + t] >= 0:
                                                min1 = min(min1, lt[i - t][j - item + t])
                    if min1 != 200000000:
                        lt[i][j] = min1 + 1
                    else:
                        lt[i][j] = -1
        for item in lt:
            print(item)
        print(lt[n][m])
