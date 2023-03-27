




"""
【约瑟夫问题】
2 1
1

2 2
0
"""

if __name__ == '__main__':
    s = input().split(' ')
    n = int(s[0])
    m = int(s[1])
    res = 0
    for i in range(1,n+1):
        res = (res+m)%i
    print(res)