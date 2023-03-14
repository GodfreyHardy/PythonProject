
"""
[最长递增子序列](3)
"""

if __name__ == '__main__':
    arr = [1,3,8,6,5,2,5]
    d = []
    res = []
    cnt = [0] * len(arr)  # 记录以arr[i]结尾元素最长上升序列长度
    i = 0
    for n in arr:
        if len(d) == 0 or d[len(d) - 1] < n:
            d.append(n)
            cnt[i] = len(d)
        else:
            left = 0
            right = len(d) - 1
            pos = 0
            flag = 0
            while left <= right:
                mid = (left + right) // 2
                if d[mid] >= n:
                    pos = mid
                    right = mid - 1
                elif d[mid] < n:
                    left = mid + 1
                else:
                    flag = 1
                    break
            if flag == 0:
                d[pos] = n
                cnt[i] = pos + 1
        i += 1
    length = len(d)
    # print(res)
    # print(length)
    print(cnt)
    for i in range(len(arr) - 1, -1, -1):
        if cnt[i] == length:
            res.append(arr[i])
            length -= 1
    res.reverse()
    print(res)
    # arrLen = len(arr)
    #
    # ansArr = [arr[0]]  # 记录某个数字结尾时最长的最长递增子序列，初始化第一个数字
    # maxLen = [1]  # 下标i时，最长的递增子序列长度，初始化1
    #
    # for a in arr[1:]:
    #     if a > ansArr[-1]:  # 当前数字大于ansArr最后一个数字，子数组保持递增
    #         ansArr.append(a)
    #         maxLen.append(len(ansArr))
    #     # 当前数字小于等于ansArr最后一个数字，二分查找ansArr中第一个比当前数字大的下标pos
    #     # 替换ansArr中下标pos的数字为当前数字，更新maxLen，记录当前最长递增子序列长度为：pos + 1(下标+1)
    #     else:
    #         pos = bisect.bisect_left(ansArr, a)
    #         ansArr[pos] = a
    #         maxLen.append(pos + 1)
    # # 找到的ansArr不一定是最终结果，[2,1,5,3,6,4,8,9,7] - > [1, 3, 4, 7, 9] (不是最终结果)
    # # [1, 1, 2, 2, 3, 3, 4, 5, 4] 从后往前遍历maxLen,依次找到等于len(arrLen)对应的 arr[i]
    # ansLen = len(ansArr)
    # print(maxLen)
    # for i in range(arrLen - 1, -1, -1):
    #     if maxLen[i] == ansLen:
    #         ansArr[ansLen - 1] = arr[i]
    #         ansLen -= 1
    # print(ansArr)