
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

if __name__ == '__main__':
    s = input().split(' ')
    t = int(s[1])
    a = int(s[2])
    b = int(s[3])
    s = int(s[0])
    diff = abs(s-t)
    d = gcd(a,b)
    if diff%d != 0:
        print('none')
    else:
        z = diff//d
        x,y = expendgcd(a,b)
        x0,y0 = x*z,y*z
        print(x)
        print(y)
        print(x0)
        print(y0)
        #x2 = x0-bm
        #y2 = y0+am
        bound = abs(x0)//b+2
        minx = 21000000000
        for m in range(bound):
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
