
"""
【对称美学】
题目描述
对称就是最大的美学，现有一道关于对称字符串的美学。
已知：
第 1 个字符串：R
第 2 个字符串：BR
第 3 个字符串：RBBR
第 4 个字符串：BRRBRBBR
第 5 个字符串：RBBRBRRBBRRBRBBR
相信你已经发现规律了，没错！
就是第i个字符串 = 第i-1号字符串的取反 + 第i-1号字符串。
取反即(R->B, B->R);
现在告诉你 n 和 k ，让你求得第n个字符串的第k个字符是多少。
(k的编号从0开始)
"""
#复杂度 2^n   1<=n<=64
def generate(n):
    if n==1:
        return '1'
    s = generate(n-1)
    pre = ''
    for i in range(len(s)):
        if s[i] == '1':
            pre += '0'
        else:
            pre += '1'
    return pre + s

#打表,动态规划计算f(n,m) 0<=m<=2^n-1


def f(n,m):
    if n==1:
        return 1
    k = pow(2,n-1)
    if m+1>k//2:
        return 1-f(n,m-(k//2))
    else:
        return 1-f(n-1,m)
    return 1

#1 01 1001 01101001
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    k = generate(n)
    print(k)
    print(k[m])
    t = f(n,m)
    print(t)
