"""
■ 题目描述
为了提升数据传输的效率，会对传输的报文进行压缩处理。
输入一个压缩后的报文，请返回它解压后的原始报文。
压缩规则：n[str]，表示方括号内部的 str 正好重复 n 次。
注意 n 为正整数（0 < n <= 100），str只包含小写英文字母，不考虑异常情况。
输入描述:
输入压缩后的报文：
1）不考虑无效的输入，报文没有额外的空格，方括号总是符合格式要求的；
2）原始报文不包含数字，所有的数字只表示重复的次数 n ，例如不会出现像 5b 或 3[8] 的输入；
输出描述:
解压后的原始报文
注：
1）原始报文长度不会超过1000，不考虑异常的情况
示例 1   输入输出示例仅供调试，后台判题数据一般不包含示例
输入
3[k]2[mn]
输出
kkkmnmn
说明
k 重复3次，mn 重复2次，最终得到 kkkmnmn
示例2  输入输出示例仅供调试，后台判题数据一般不包含示例
输入
3[m2[c]]3[k]2[mn]
输出
mccmccmcc
说明
3[m2[a2[c]]]3[k]2[mn]
m2[c] 解压缩后为 mcc，重复三次为 mccmccmcc
"""


def build(s, begin, res):
    if begin[0] == len(s):
        return res
    k = ""
    while ord('0') <= ord(s[begin[0]]) <= ord('9'):
        k += s[begin[0]]
        begin[0] += 1
    k = int(k)
    begin[0] += 1
    tmp = ""
    while ord('a') <= ord(s[begin[0]]) <= ord('z'):
        tmp += s[begin[0]]
        begin[0] += 1
    if s[begin[0]]==']':
        begin[0] += 1
        for i in range(k):
            res += tmp
        if begin[0]<len(s) and ord('0') <= ord(s[begin[0]]) <= ord('9'):
            res += build(s,begin,"")
        elif begin[0]<len(s) and s[begin[0]]==']':
            return res
        else:
            return res
    elif ord('0') <= ord(s[begin[0]]) <= ord('9'):
        tmps = build(s,begin,"")
        tmp += tmps
        for i in range(k):
            res += tmp
        begin[0] += 1
        if begin[0]<len(s) and ord('0') <= ord(s[begin[0]]) <= ord('9'):
            res += build(s,begin,"")
        elif begin[0]<len(s) and s[begin[0]]==']':
            return res
        else:
            return res
    return res



if __name__ == '__main__':
    res = ""
    begin = [0]
    s = input()
    res = build(s, begin, res)
    print(res)












