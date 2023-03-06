def days_needed(k, fields):
    days = 0
    for field in fields:
        days += (field + k - 1) // k
    return days

def min_fertilizer(fields, n):
    l = 1               # 施肥机能效的可能取值范围：[1, max(fields)]
    r = max(fields)
    while l < r:
        mid = (l + r) // 2
        if days_needed(mid, fields) <= n:
            r = mid
        else:
            l = mid + 1
    return l

if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[0])
    k = int(s[1])
    s = input()
    s = s.split(' ')
    lt = []
    dic = {}
    for i in range(n):
        lt.append(int(s[i]))
        dic[int(s[i])] = 1
    if k < n:
        print(-1)
    else:
        res = min_fertilizer(lt,k)
        print(res)