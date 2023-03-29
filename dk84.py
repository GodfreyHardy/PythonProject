
"""
【完美走位】
"""



def check(tmp,dic,d,k):
    lt = [0]*4
    lt[0] = dic[0] - tmp[0]
    lt[1] = dic[1] - tmp[1]
    lt[2] = dic[2] - tmp[2]
    lt[3] = dic[3] - tmp[3]
    if d<lt[0] or d<lt[1] or d<lt[2] or d<lt[3]:
        return False
    if 4*d-(lt[0]+lt[1]+lt[2]+lt[3]) != k:
        return False
    return True




if __name__ == '__main__':
    s = input()
    dic = [0]*4
    for i in range(len(s)):
        if s[i] == 'W':
            dic[0] += 1
        elif s[i] == 'S':
            dic[1] += 1
        elif s[i] == 'A':
            dic[2] += 1
        elif s[i] == 'D':
            dic[3] += 1
    if len(s) % 4 != 0:
        print(-1)
    elif dic[0]==dic[1]==dic[2]==dic[3]:
        print(0)
    else:
        left = 0
        right = 0
        tmp = [0]*4
        min1 = 2147483647
        if s[left] == 'W':
            tmp[0] += 1
        elif s[left] == 'S':
            tmp[1] += 1
        elif s[left] == 'A':
            tmp[2] += 1
        elif s[left] == 'D':
            tmp[3] += 1
        while right < len(s):
            if not check(tmp, dic,len(s)//4,right-left+1):
                right += 1
                if right < len(s):
                    if s[right] == 'W':
                        tmp[0] += 1
                    elif s[right] == 'S':
                        tmp[1] += 1
                    elif s[right] == 'A':
                        tmp[2] += 1
                    elif s[right] == 'D':
                        tmp[3] += 1
            else:
                min1 = min(min1, right-left+1)
                if s[left] == 'W':
                    tmp[0] += 1
                elif s[left] == 'S':
                    tmp[1] += 1
                elif s[left] == 'A':
                    tmp[2] += 1
                elif s[left] == 'D':
                    tmp[3] += 1
                left += 1
        print(min1)