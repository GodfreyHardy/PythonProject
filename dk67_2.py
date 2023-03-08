




"""
10,9,2,5,3,7,101,18
4
4,10,4,3,8,9
3
1,3,6,7,9,4,10,5,6
"""
if __name__ == '__main__':
    nums = []
    s = input()
    s = s.split(',')
    for i in range(len(s)):
        nums.append(int(s[i]))
    length = 1
    d = []
    d.append(nums[0])
    for i in range(1,len(nums)):
        if nums[i] > d[length-1]:
            length += 1
            d.append(nums[i])
        elif nums[i] < d[length-1]:
            left = 0
            right = length-1
            mid = (left+right)//2
            flag = 0
            pos = 0
            while left <= right:
                if nums[i] < d[mid]:
                    right = mid - 1
                    pos = mid
                elif nums[i] > d[mid]:
                    left = mid + 1
                else:
                    flag = 1
                    break
                mid = (left + right) // 2
            if flag == 0:
                d[pos] = nums[i]
    print(d)



