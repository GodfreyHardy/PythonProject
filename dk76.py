


"""
【查找充电设备组合】
某个充电站，可提供n个充电设备，每个充电设备均有对应的输出功率。
任意个充电设备组合的输出功率总和，均构成功率集合P的1个元素。
功率集合P的最优元素，表示最接近充电站最大输出功率p_max的元素
输入为3行
第1行为充电设备个数n
第2行为每个充电设备的输出功率
第3行为充电站最大输出功率p_max
功率集合P的最优元素

输入
4
50 20 20 60
90
输出
90

输入
2
50 40
30
输出
0

"""

if __name__ == '__main__':
    n = int(input())
    s = input().split(' ')
    lt = []
    for i in range(n):
        lt.append(int(s[i]))
    target = int(input())
    dp = [0]*(target+1)
    for i in range(n):
        for j in range(target, lt[i]-1, -1):
            dp[j] = max(dp[j], dp[j-lt[i]]+lt[i])
    print(dp[target])




