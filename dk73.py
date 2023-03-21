
"""
[扩展欧几里得算法]
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def expendgcd(a,b):
    if b == 0:
        return 1,0
    x,y = expendgcd(b,a%b)
    return y,x-(a//b)*y

#最容易忽略的一个思路

def calculate(s,t,a,b):
    # t = s+n*a+m*b
    # t-s-n*a = m*b
    #遍历n的值
    n = 0
    diff = t - s
    while 1:
        k1 = diff - n*a
        k2 = diff + n*a
        if k1%b==0 or k2%b==0:
            break
        n += 1
    print(n)


if __name__ == '__main__':
    s = input().split(' ')
    t = int(s[1])
    a = int(s[2])
    b = int(s[3])
    s = int(s[0])
    calculate(s,t,a,b)
    diff = abs(s-t)
    d = gcd(a,b)
    if diff%d != 0:
        print('none')
    else:
        z = diff//d
        x,y = expendgcd(a,b)
        x0,y0 = x*z,y*z
        # print(x)
        # print(y)
        # print(x0)
        # print(y0)
        #x2 = x0-bm
        #y2 = y0+am
        bound = abs(x0)//b+2
        # print(bound)
        minx = 21000000000
        for m in range(bound,bound-4,-1):
            if abs(x0-b*m) < minx:
                minx = abs(x0-b*m)
            if abs(x0+b*m) < minx:
                minx = abs(x0+b*m)
        print(minx)

"""
1 10 5 2
1

11 33 4 10
2
"""
