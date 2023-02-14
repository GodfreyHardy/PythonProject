"""
■ 题目描述
【无向图染色】
题目描述
给一个无向图染色，可以填红黑两种颜色，必须保证相邻两个节点不能同时为红色，输出有多少种不同的染色方案？
输入描述
第一行输入M(图中节点数) N(边数)
后续N行格式为：V1 V2表示一个V1到V2的边。
数据范围：1 <= M <= 15,0 <= N <= M * 3，不能保证所有节点都是连通的。
输出描述
输出一个数字表示染色方案的个数。
示例1  输入输出示例仅供调试，后台判断数据一般不包含示例
输入
4 4
1 2
2 4
3 4
1 3
输出
7
说明
4个节点，4条边，1号节点和2号节点相连，
2号节点和4号节点相连，3号节点和4号节点相连，
1号节点和3号节点相连，
若想必须保证相邻两个节点不能同时为红色，总共7种方案。
"""


# 删去相邻节点同时为红色的情况

def check(dic, sequence):
    for key in dic:
        s = key.split('#')
        i = int(s[0]) - 1
        j = int(s[1]) - 1
        if sequence[i] == '0' and sequence[j] == '0':
            return False
    return True


def ergodic(n, vec, dic, sequence):
    if n == 0:
        if check(dic,sequence):
            vec[0] += 1
        return
    for i in range(2):
        if i == 0:
            ergodic(n - 1, vec, dic, sequence + '0')
        else:
            ergodic(n - 1, vec, dic, sequence + '1')

    return


if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    m = int(s[1])
    dic = {}
    for i in range(m):
        s = input()
        s = s.split(' ')
        dic[s[0] + '#' + s[1]] = 1
    vec = [0]
    ergodic(n, vec, dic, '')
    print(vec)
