







if __name__ == '__main__':
    n = int(input())
    s = input().split(' ')
    lt = [int(x) for x in s]
    res = [0]*n
    dp = [-1]*n
    res[n-1] = lt[n-1]
    for i in range(n-2,-1,-1):
        j = i+1
        while j < n:
            if lt[j] > lt[i]:
                dp[i] = j
                break
            elif lt[j] == lt[i]:
                dp[i] = dp[j]
                break
            else:#lt[j]<lt[i]
                j = dp[j]
                if j == -1:
                    break
    for i in range(n):
        if dp[i] == -1:
            res[i] = lt[i]
        else:
            res[i] = (dp[i]-i)*(lt[dp[i]]-lt[i])
    ans = ''
    for i in range(n):
        ans += str(res[i])
        if i != n-1:
            ans += ' '
    print(ans)