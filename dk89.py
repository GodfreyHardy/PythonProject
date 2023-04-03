





"""
【字符串重新排序】
"""
def sortbyarr(arr):
    for i in range(len(arr)):
        arr[i] = ''.join(sorted(arr[i]))
    dic = {}
    #print(arr)
    for a in arr:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    arr.sort(key=lambda x:(-dic[x],len(x),x))
    print(' '.join(map(str,arr)))

if __name__ == '__main__':
    s = input().split(' ')
    lt = []
    dic = {}
    sortbyarr(s)
    for i in range(len(s)):
        tmp = list(s[i])
        tmp.sort()
        #print(tmp)
        tmp = ''.join(tmp)
        if tmp not in dic:
            dic[tmp] = [1,len(tmp)]
        else:
            dic[tmp][0] += 1
    a = sorted(dic.items(),key=lambda x:(-x[1][0],x[1][1],x[0]))
    res = ''
    for i in range(len(a)):
        for j in range(a[i][1][0]):
            res += a[i][0]+' '
    print(res[0:len(res)-1])
"""
This is an apple
an is This aelpp

My sister is in the house not in the yard
in in eht eht My is not adry ehosu eirsst
"""