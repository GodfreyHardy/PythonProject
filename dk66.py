"""
■ 题目描述
【不爱施肥的小布】
input:
5 7
5 7 9 15 10
output:
9
input:
3 1
2 3 4
output:
-1
"""


# 1<=length<=10000
# 1<=lt[i]<=10^9


# 二分搜索

def cmp(lt, midval):
    res = 0
    for i in range(len(lt)):
        res += (lt[i] + midval - 1) // midval  # //向下取整
    return res


if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    k = int(s[1])
    s = input()
    s = s.split(' ')
    lt = []
    for i in range(n):
        lt.append(int(s[i]))
    lt.sort()
    if k < n:
        print(-1)
    else:
        l = 1
        r = lt[n - 1]
        mid = (l + r) // 2
        while l < r:
            if cmp(lt, mid) <= k:
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2
        print(mid)
