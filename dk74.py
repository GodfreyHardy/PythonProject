

"""
■ 题目描述
【递增字符串】
定义字符串完全由 ‘A’ 和 ‘B’组成，当然也可以全是’A’或全是’B’。
如果字符串从前往后都是以字典序排列的，那么我们称之为严格递增字符串。
给出一个字符串s，允许修改字符串中的任意字符，即可以将任何的’A’修改成’B’，
也可以将任何的’B’修改成’A’，求可以使s满足严格递增的最小修改次数。
0 < s的长度 < 100000。
"""



if __name__ == '__main__':
    s = input()
    #从左往右 从右往左
    pos = -1
    for i in range(len(s)):
        if s[i]=='B':
            pos = i
            break
    resb = 0
    if pos != -1:
        for i in range(pos+1,len(s)):
            if s[i]=='A':
                resb += 1
    resa = 0
    pos = -1
    for i in range(len(s)-1,-1,-1):
        if s[i]=='A':
            pos = i
            break
    if pos != -1:
        for i in range(pos-1,-1,-1):
            if s[i]=='B':
                resa += 1
    res = min(resa,resb)
    print(res)