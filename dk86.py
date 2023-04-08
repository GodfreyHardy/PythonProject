#
# """
# 【最小区间覆盖】
# """
#
#
#
#
if __name__ == '__main__':
    n = int(input())
    mt = []
    for i in range(n):
        s = input().split(',')
        tmp = [int(s[0]),int(s[1])]
        mt.append(tmp)
    mt.sort(key=lambda x:(x[0],x[1]))
    print(mt)
    i = 0
    lt = []
    # 贪心思路 寻找 right_i > left_j (j>i)中right_j最大的
    while i < len(mt):
        leftval = mt[i][0]
        rightval = mt[i][1]
        while i+1<len(mt) and leftval==mt[i+1][0]:
            rightval = max(rightval,mt[i+1][1])
            i += 1
        lt.append([leftval,rightval])
        i += 1
    lt.sort(key=lambda x:(x[0],x[1]))
    lval = lt[0][0]
    rval = lt[0][1]
    res = 1
    i = 1
    st = [[lval,rval]]
    while i < len(lt):
        j = i
        top = st[-1]
        maxr = top[1]
        flag = 0
        while j < len(lt) and top[1] >= lt[j][0]:
            if maxr < lt[j][1]:
                max = lt[j][1]
                flag  = 1
            j += 1
        if maxr != top[1]:
            st.pop()
            st.append([top[0],maxr])
            res += 1
            i = j
        else:
            if i == j:
                st.append([lt[i][0],lt[i][1]])
                res += 1
                i += 1
            else:
                i = j
    print(res)
    print(st)




# if __name__ == '__main__':
#     n = int(input())  # 读入n
#
#     ranges = []  # 定义一个n行2列的二维数组ranges
#     for i in range(n):  # 循环读入n个区间
#         str_ = input().split(",")  # 读入字符串并用逗号分隔
#         ranges.append([int(str_[0]), int(str_[1])])  # 第一个数字作为区间起点，第二个数字作为区间终点
#
#     ranges.sort(key=lambda x: x[0])  # 按照区间起点从小到大排序
#
#     stack = []  # 定义一个栈
#     stack.append(ranges[0])  # 将第一个区间加入栈中
#
#     for i in range(1, len(ranges)):  # 循环处理剩余的区间
#         range_ = ranges[i]  # 取出当前区间
#         while True:  # 不断进行以下判断，直到当前区间被处理完毕
#             if not stack:  # 如果栈为空，将当前区间加入栈中
#                 stack.append(range_)
#                 break
#             top = stack[-1]  # 取出栈顶区间
#             s0, e0 = top[0], top[1]  # 栈顶区间的起点和终点
#             s1, e1 = range_[0], range_[1]  # 当前区间的起点和终点
#             if s1 <= s0:  # 如果当前区间的起点在栈顶区间内或者相等
#                 if e1 <= s0:  # 如果当前区间被栈顶区间包含
#                     break  # 直接退出循环
#                 elif e1 < e0:  # 如果当前区间的终点在栈顶区间内
#                     break  # 直接退出循环
#                 else:  # 如果当前区间的终点在栈顶区间的右边
#                     stack.pop()  # 将栈顶区间弹出
#             elif s1 < e0:  # 如果当前区间的起点在栈顶区间的右边但是和栈顶区间相交
#                 if e1 <= e0:  # 如果当前区间被栈顶区间包含
#                     break  # 直接退出循环
#                 else:  # 如果当前区间的终点在栈顶区间的右边
#                     stack.append([e0, e1])  # 将栈顶区间的终点和当前区间的终点作为新的区间加入栈中
#                     break  # 直接退出循环
#             else:  # 如果当前区间的起点在栈顶区间的右边且不相交
#                 stack.append(range_)  # 将当前区间加入栈中
#                 break  # 直接退出循环
#
#     print(len(stack))  # 返回栈的大小
