


"""
【组合出合法最小数】
题目描述
给一个数组，数组里面哦都是代表非负整数的字符串，将数组里所有的数值[排列组合]拼接起来组成一个数字，输出拼接成的最小的数字。
输入描述
一个数组，数组不为空，数组里面都是代表非负整数的字符串，可以是0开头，例如：[“13”, “045”, “09”, “56”]。
数组的大小范围：[1, 50]
数组中每个元素的长度范围：[1, 30]
输出描述
以字符串的格式输出一个数字，
如果最终结果是多位数字，要优先选择输出不是“0”开头的最小数字
如果拼接出来的数字都是“0”开头，则选取值最小的，并且把开头部分的“0”都去掉再输出
如果是单位数“0”，可以直接输出“0”
用例
示例1
输入:
20 1
输出:
120
示例2
输入:
08 10 2
输出:
10082
"""
import functools


def cmp(a, b):
    if a+b < b+a:
        return -1
    elif a+b == b+a:
        return 0
    return 1



if __name__ == '__main__':
    s = input().split(' ')
    s.sort(key=functools.cmp_to_key(cmp))
    print(s)
    if s[0][0] == '0':
        for i in range(1,len(s)):
            if s[i][0] != '0':
                s[0] = s[i]+s[0]
                s[i] = ''
                break
    res = ''
    for i in range(len(s)):
        res += s[i]
    pos = -1
    ans = res.lstrip('0')
    print(ans)
    for i in range(len(res)):
        if res[i] != '0':
            pos = i
            break
    if pos == -1:
        print('0')
    else:
        print(res[pos:len(res)])










