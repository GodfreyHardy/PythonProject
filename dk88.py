



"""
【知识图谱新词挖掘】
"""

if __name__ == '__main__':
    # 滑动窗口
    s = input()
    word = input()
    dic = {}
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 1
        else:
            dic[word[i]] += 1
    left = 0
    right = 0
    tmp = {}
    if len(s) < len(word):
        print(0)
    else:
        while right < len(word):
            if s[right] not in tmp:
                tmp[s[right]] = 1
            else:
                tmp[s[right]] += 1
            right += 1
        res = 0
        if tmp == dic:
            res = 1
        while right < len(s):
            if s[right] not in tmp:
                tmp[s[right]] = 1
            else:
                tmp[s[right]] += 1
            tmp[s[left]] -= 1
            if tmp[s[left]] == 0:
                tmp.pop(s[left])
            print(tmp)
            print(dic)
            if tmp == dic:
                res += 1
            left += 1
            right += 1
        print(res)
"""
qweebaewqd
qwe
2

abab
ab
3
"""

