"""
■ 题目描述
【单词搜索】
找到它是一个小游戏，你需要在一个矩阵中找到给定的单词。
假设给定单词 HELLOWORD，在矩阵中只要能找到 H->E->L->L->O->W->O->R->L->D连成的单词，就算通过。
注意区分英文字母大小写，并且您只能上下左右行走，不能走回头路。
输入描述
输入第 1 行包含两个整数 n、m (0 < n,m < 21) 分别表示 n 行 m 列的矩阵，
第 2 行是长度不超过100的单词 W (在整个矩阵中给定单词 W 只会出现一次)，
从第 3 行到第 n+2 行是指包含大小写英文字母的长度为 m 的字符串矩阵。
输出描述
如果能在矩阵中连成给定的单词，则输出给定单词首字母在矩阵中的位置(第几行 第几列)，
否则输出“NO”。
示例1  输入输出示例仅供调试，后台判题数据一般不包含示例
输入
5 5
HELLOWORLD
CPUCY
EKLQH
CHELL
LROWO
DGRBC
输出
3 2
"""


def search(lt, target, sign, begin, row, col, res):
    if begin == len(target):
        return res
    # 回溯算法 四个方向
    if row - 1 >= 0 and sign[row - 1][col] == 0 and lt[row - 1][col] == target[begin]:
        sign[row - 1][col] = 1
        if search(lt, target, sign, begin + 1, row - 1, col, res) != '':
            return res
        sign[row - 1][col] = 0
    if row + 1 < len(lt) and sign[row + 1][col] == 0 and lt[row + 1][col] == target[begin]:
        sign[row + 1][col] = 1
        if search(lt, target, sign, begin + 1, row + 1, col, res) != '':
            return res
        sign[row + 1][col] = 0
    if col - 1 >= 0 and sign[row][col - 1] == 0 and lt[row][col - 1] == target[begin]:
        sign[row][col - 1] = 1
        if search(lt, target, sign, begin + 1, row, col - 1, res) != '':
            return res
        sign[row][col - 1] = 0
    if col + 1 < len(lt[0]) and sign[row][col + 1] == 0 and lt[row][col + 1] == target[begin]:
        sign[row][col + 1] = 1
        if search(lt, target, sign, begin + 1, row, col + 1, res) != '':
            return res
        sign[row][col + 1] = 0
    return ''


if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    m = int(s[1])
    target = input()
    lt = [['0'] * m for _ in range(n)]
    for i in range(n):
        line = input()
        for j in range(m):
            lt[i][j] = line[j]
    sign = [[0] * m for _ in range(n)]
    ans = ''
    flag = 0
    for i in range(0, len(lt)):
        for j in range(0, len(lt[0])):
            if sign[i][j] == 0 and lt[i][j] == target[0]:
                sign[i][j] = 1
                res = str(i + 1) + ' ' + str(j + 1)
                ans = search(lt, target, sign, 1, i, j, res)
                if ans != '':
                    flag = 1
                    break
        if flag:
            break
    print(ans)
