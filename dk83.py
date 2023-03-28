
def check(tmp ,dic):
    for key in dic:
        if key not in tmp or tmp[key ] <dic[key]:
            return False
    return True




if __name__ == '__main__':
    s = input()
    t = input()
    dic = {}
    for i in range(len(t)):
        if t[i] not in dic:
            dic[t[i]] = 1
        else:
            dic[t[i]] += 1
    left = 0
    right = 0
    tmp = {}
    res = [0, 0]
    min1 = 2147483647
    tmp[s[left]] = 1
    flag = 0
    while right < len(s):
        if not check(tmp, dic):
            right += 1
            if right < len(s) and s[right] not in tmp:
                tmp[s[right]] = 1
            elif right < len(s) and s[right] in tmp:
                tmp[s[right]] += 1
        else:
            flag = 1
            if min1 > right -left +1:
                min1 = right - left + 1
                res[0] = left
                res[1] = right
            tmp[s[left]] -= 1
            left += 1
    if flag == 0:
        print('')
    else:
        print(s[res[0]:res[1] + 1])
"""
ADOBECODEBANC
ABC

a
a
"""