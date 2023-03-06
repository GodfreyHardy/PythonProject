
# 复杂度为O(n^2)
n = int(input())
s = input()
s = s.split(' ')
#print(s)
lt = []
for i in range(len(s)):
    lt.append(int(s[i]))
left = [1]*len(lt)
right = [1]*len(lt)
for i in range(1,n):
    for j in range(0,i):
        if lt[i] > lt[j]:
            left[i] = max(left[i],left[j]+1)
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if lt[i] > lt[j]:
            right[i] = max(right[i],right[j]+1)
res = 2147483647
print(left)
print(right)
for i in range(n):
    k = right[i] + left[i] - 1
    res = min(res,n-k)
print(res)