"""
input:
010
output:
1
input:
1101210
output:
3
"""
if __name__ == '__main__':
    s = input()
    lt = []
    #len(s)<=100000
    lt0 = []
    lt2 = []
    lt3 = []
    for i in range(len(s)):
        lt.append(int(s[i]))
        if s[i] == '0' or s[i] == '2':
            lt3.append(i)
            if s[i] == '0':
                lt0.append(i)
            else:
                lt2.append(i)
    if len(lt0) == 0:
        print(-1)
    else:
        lt3.sort()
        res = 0
        pos = 0
        for i in range(len(lt0)):
            left = 0
            right = 0
            for j in range(pos,len(lt3)):
                if lt3[j] == lt0[i]:
                    pos = j
                    break
            if pos == 0:
                left = -1
            else:
                left = lt3[pos-1]
            if pos == len(lt3)-1:
                right = len(lt)
            else:
                right = lt3[pos+1]
            leftval = lt3[pos] - left - 1
            rightval = right - lt3[pos] - 1
            res = max(res,leftval+rightval)
        print(res)