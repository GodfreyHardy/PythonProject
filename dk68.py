"""
■ 题目描述
【单向链表中间节点】
题目描述
求单向链表中间的节点值，如果奇数个节点取中间，偶数个取偏右边的那个值。
输入：
第一行 链表头节点地址 后续输入的节点数n
后续输入每行表示一个节点，格式 节点地址 节点值 下一个节点地址(-1表示空指针)
输入保证链表不会出现环，并且可能存在一些节点不属于链表。
测试用例:
输入:
00010 4
00000 3 -1
00010 5 12309
11451 6 00000
12309 7 11451
输出:
6
"""


if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[1])
    head = s[0]
    lt = []
    dic = {}
    for i in range(n):
        s = input()
        s = s.split(' ')
        dic[s[0]] = s[1] + '#' + s[2]
    # 并且可能存在一些节点不属于链表 need to fix the bug
    while head in dic:
        val = dic[head].split('#')
        lt.append(val[0])
        head = val[1]
        if val[1]=='-1':
            break
    print(lt)
    print(lt[n // 2])
