
def lengthOfLongestSubstring(s):
    dic = {}
    res = 0
    begin = 0
    cur = 0
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
            cur += 1
        else:
            if dic[s[i]] < begin:
                cur += 1
            else:
                begin = dic[s[i]] + 1
                cur = i-begin+1
            dic[s[i]] = i
        res = max(cur,res)
    return res

"""
input:
abcabcbb
output:
3
"""
if __name__ == '__main__':
    s = input()
    res = lengthOfLongestSubstring(s)
    print(res)