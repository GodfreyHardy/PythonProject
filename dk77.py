



"""
[放苹果]
描述
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。
数据范围：
0≤m≤10
1≤n≤10
输入描述：
输入两个int整数
输出描述：
输出结果，int型
7 3
8
"""

if __name__ == '__main__':
    s = input().split(' ')
    m = int(s[0])
    n = int(s[1])
    if n > m:
        n = m
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    # dp[i][j] = dp[i-1][j-1]+dp[i-j][j]
    # n<=m
    for i in range(1, m + 1):
        dp[i][1] = 1
    for i in range(2, m + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    for item in dp:
        print(item)
    res = 0
    for i in range(n):
        res += dp[m][n - i]
    print(res)