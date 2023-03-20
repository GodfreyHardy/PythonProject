





if __name__ == '__main__':
    n = int(input())
    s = input()
    s = s.split(' ')
    #print(s)
    lt = []
    for i in range(len(s)):
        lt.append(int(s[i]))
    left = [1]*len(lt)
    d = []
    d.append(lt[0])
    for i in range(1,n):
        if lt[i] > d[len(d)-1]:
            d.append(lt[i])
            left[i] = len(d)
        else:
            l = 0
            r = len(d)-1
            pos = -1
            while l <= r:
                mid = (l+r)//2
                if lt[i] > d[mid]:
                    l = mid + 1
                else:
                    pos = mid
                    r = mid - 1
            if pos != -1:
                left[i] = pos+1
                d[pos] = lt[i]
        print(d)
    lt2 = lt[::-1]
    right = [1] * len(lt)
    d = []
    d.append(lt2[0])
    for i in range(1,n):
        if lt2[i] > d[len(d)-1]:
            d.append(lt2[i])
            right[i] = len(d)
        else:
            l = 0
            r = len(d)-1
            pos = -1
            while l <= r:
                mid = (l+r)//2
                if lt2[i] > d[mid]:
                    l = mid + 1
                else:
                    pos = mid
                    r = mid - 1
            if pos != -1:
                right[i] = pos+1
                d[pos] = lt2[i]
    right = right[::-1]
    print(left)
    print(right)
    res = 2147483647
    for i in range(n):
        k = right[i] + left[i]-1
        res = min(res,n-k)
    print(res)
    """
    [1, 2, 3, 2, 4, 3, 4, 4]
    [1, 2, 2, 1, 3, 1, 2, 1]
    2
    """
    # n = int(input())
    # s = input()
    # s = s.split(' ')
    # # print(s)
    # lt = []
    # for i in range(len(s)):
    #     lt.append(int(s[i]))
    # left = [1] * len(lt)
    # right = [1] * len(lt)
    # for i in range(1, n):
    #     for j in range(0, i):
    #         if lt[i] > lt[j]:
    #             left[i] = max(left[i], left[j] + 1)
    # for i in range(n - 2, -1, -1):
    #     for j in range(i + 1, n):
    #         if lt[i] > lt[j]:
    #             right[i] = max(right[i], right[j] + 1)
    # res = 2147483647
    # print(left)
    # print(right)
    # for i in range(n):
    #     k = right[i] + left[i] - 1
    #     res = min(res, n - k)
    # print(res)