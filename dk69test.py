


def cal(s):
    s = s.replace('//', '/')
    op = []
    d = []
    i = 0
    while i < len(s):
        tmp1 = ''
        while i<len(s) and ord('0')<=ord(s[i])<=ord('9'):
            tmp1 += s[i]
            i += 1
        d.append(int(tmp1))
        if i<len(s):
            op.append(s[i])
        i += 1
    print(d)
    print(op)
    print('................')
    while len(d)>0 and len(op)>0:
        d1 = d.pop(0)
        d2 = d.pop(0)
        k = op.pop(0)
        d3 = 0
        if k=='+':
            d3 = d1 + d2
        elif k=='-':
            d3 = d1 - d2
        elif k=='*':
            d3 = d2 * d1
        elif k=='/':
            d3 = d1 // d2
        d.insert(0,d3)
        print(d)
    print(d)
    return d[0]

if __name__ == '__main__':
    print(cal('4*2-13-1'))