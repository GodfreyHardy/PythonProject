


"""
【挑选字符串】
给定a-z，26个英文字母小写字符串组成的字符串A和B，
其中A可能存在重复字母，B不会存在重复字母，现从字符串A中按规则挑选一些字母可以组成字符串B挑选规则如下:
1：同一个位置的字母只能挑选一次，
2：被挑选字母的相对先后顺序不能被改变，
求最多可以同时从A中挑选多少组能组成B的字符串
输入描述：
输入为2行，
第一行输入字符串a,第二行输入字符串b，行首行尾没有多余空格
输出描述：
输出一行
包含一个数字表示最多可以同时从a中挑选多少组能组成b的字符串，行末没有多余空格
示例一
输入
badc
bac
输出
1
示例二
输入
badc
abc
输出
0
示例三
输入
bbadcac
bac
输出
2
"""




if __name__ == '__main__':
    a = input()
    n = len(a)
    b = input()
    m = len(b)
    dic = {}
    for i in range(len(b)):
        dic[b[i]] = i
    res = [0]*len(b)
    for i in range(len(a)):
        if a[i] in dic:
            pos = dic[a[i]]
            if pos==0 or res[pos]<res[pos-1]:
                res[pos] += 1
    print(res)
    print(res[-1])




