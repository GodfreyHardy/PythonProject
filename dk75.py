"""
【寻找相似单词】
给定一个可存储若干单词的字典，找出指定单词的所有相似单词，并且按照单词名称从小到大排序输出。
单词仅包括字母，但可能大小写并存（大写不一定只出现在首字母）。
相似单词说明：给定一个单词X，如果通过任意交换单词中字母的位置得到不同的单词Y，
那么定义Y是X的相似单词，如abc、bca即为相似单词（大小写是不同的字母，如a和A算两个不同字母）。
字典序排序： 大写字母<小写字母。同样大小写的字母，遵循26字母顺序大小关系。
即A<B<C<…<X<Y<Z<a<b<c<…<x<y<z. 如Bac<aBc<acB<cBa.
输入描述
第一行为给定的单词个数N（N为非负整数）
从第二行到地N+1行是具体的单词（每行一个单词）
最后一行是指定的待检测单词（用于检测上面给定的单词中哪些是与该指定单词是相似单词，该单词可以不是上面给定的单词）
输出描述
从给定的单词组中，找出指定单词的相似单词，并且按照从小到大字典序排列输出，中间以空格隔开
如果不存在，则输出null（字符串null）
"""


if __name__ == '__main__':
    n = int(input())
    lt = []
    for i in range(n):
        s = input()
        lt.append(s)
    target = input()
    dic = {}
    p = []
    for i in range(len(target)):
        if target[i] not in dic:
            dic[target[i]] = 1
        else:
            dic[target[i]] += 1
    for i in range(n):
        if lt[i]!=target and len(target)==len(lt[i]):
            z = {}
            for j in range(len(target)):
                if lt[i][j] not in z:
                    z[lt[i][j]] = 1
                else:
                    z[lt[i][j]] += 1
            if dic==z:
                p.append(lt[i])
    if len(p)==0:
        print('null')
    else:
        p.sort()
        print(p)

