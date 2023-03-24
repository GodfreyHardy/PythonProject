"""
■ 题目描述
【优雅子数组】
如果一个数组中出现次数最多的元素出现大于等于K次，被称为 k-优雅数组 ，k也可以被称为优雅阈值。
例如，
数组1,2,3,1,2,3,1，它是一个3-优雅数组，因为元素1出现次数大于等于3次，
数组[1, 2, 3, 1, 2]就不是一个3-优雅数组，因为其中出现次数最多的元素是1和2，只出现了2次。
给定一个数组A和k，请求出A有多少子数组是k-优雅子数组。
子数组是数组中一个或多个连续元素组成的数组。
例如，数组[1,2,3,4]包含10个子数组，分别是：
[1], [1,2], [1,2,3], [1,2,3,4], [2], [2,3], [2,3,4], [3], [3, 4], [4]。
"""

if __name__ == '__main__':
    s = input()
    s = s.split(',')
    lt = []
    for item in s:
        lt.append(int(item))
    left = 0
    right = 0
    dic = {}
    pre = -1
    res = 0
    #以lt[i]开头的符合k>=3的数量
    while left <= right < len(lt):
        if pre != right:
            if lt[right] not in dic:
                dic[lt[right]] = 1
            else:
                dic[lt[right]] += 1
            pre = right
        if dic[lt[right]] >= 3:
            dic[lt[left]] -= 1
            left += 1
            res += len(lt)-right
        else:
            right += 1
    print(res)