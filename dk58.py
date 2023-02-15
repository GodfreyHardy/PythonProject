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
若想必须保证相邻两个节点不能同时为红色，总共10种方案。
"""


# 模拟染色情况

def search(lt,  vec, begin, sequence):
    if begin == len(lt):
        vec[0] += 1
        return
    num = 0
    for i in range(len(lt[begin])):
        if lt[begin][i] == 1 and sequence[i] == '0':
            num += 1
            break
    if num > 0:
        sequence[begin] = '1'
        search(lt,vec,begin+1,sequence)
    else:
        sequence[begin] = '0'
        search(lt, vec, begin + 1, sequence)
        sequence[begin] = '1'
        search(lt, vec, begin + 1, sequence)
    return


if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    m = int(s[1])
    lt = [[0] * n for _ in range(n)]
    for i in range(m):
        s = input()
        s = s.split(' ')
        lt[int(s[0]) - 1][int(s[1]) - 1] = 1
        lt[int(s[1]) - 1][int(s[0]) - 1] = 1
    vec = [0]
    search(lt,  vec, 0,[-1]*n)
    print(vec[0])
