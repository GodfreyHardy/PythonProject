"""
给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。
您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。
"""


if __name__ == '__main__':
    num = []
    s = input()
    s = s.split(' ')
    arr = []
    for i in range(0, len(s)):
        arr.append(int(s[i]))
    k = 1
    m = 10
    for i in range(0, 10):  # 复杂度O(10*N)
        base = [[] for _ in range(10)]
        for j in range(0, len(arr)):
            index = (arr[j] % m) * 10 // m  # 从个位数开始向最高位遍历取对应位数上的值
            base[index].append(arr[j])
        m *= 10
        pos = 0
        print(base)
        for i2 in range(0, 10):
            for j2 in range(0, len(base[i2])):
                arr[pos] = base[i2][j2]
                pos += 1
    print(arr)
# 11 15 12 13 14 22 254 121156
