





"""
【最多几个三角形】
"""

max1 = -1

def judge(dic):
    num = []
    for key in dic:
        for i in range(dic[key]):
            num.append(key)
    if len(num) < 3:
        return True
    num.sort()
    for i in range(len(num)-2):
        for j in range(i+1,len(num)-1):
            for k in range(j+1,len(num)):
                if num[i]*num[i]+num[j]*num[j]==num[k]*num[k]:
                    return False
    return True
def combine(dic,res,ans,num,begin):
    global max1
    if judge(dic):#bug
        tmp = []
        tmp.extend(num)
        print(num)
        max1 = max(max1,len(num))
        ans.append(tmp)
        return ans
    for i in range(begin,len(res)):
        a = res[i][0]
        b = res[i][1]
        c = res[i][2]
        if dic[a]>0 and dic[b]>0 and dic[c]>0:
            dic[a] -= 1
            dic[b] -= 1
            dic[c] -= 1
            num.append([a,b,c])
            combine(dic,res,ans,num,i+1)
            num.pop()
            dic[a] += 1
            dic[b] += 1
            dic[c] += 1
    return ans



def search(lt,begin,res,num):
    if len(num) == 3:
        if num[0]*num[0]+num[1]*num[1]==num[2]*num[2]:
            item = []
            item.extend(num)
            res.append(item)
            return res
    for i in range(begin,len(lt)):
        num.append(lt[i])
        search(lt,i+1,res,num)
        num.pop()
    return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().split(' ')
        lt = []
        dic = {}
        for j in range(1,len(s)):
            lt.append(int(s[j]))
            if int(s[j]) not in dic:
                dic[int(s[j])] = 1
            else:
                dic[int(s[j])] += 1
        lt.sort()
        res = []
        res = search(lt,0,res,[])
        print(res)
        print(dic)
        ans = []
        combine(dic,res,ans,[],0)
        print(ans)
        print(max1)
"""
1
7 3 4 5 6 5 12 13
2

1
7 3 4 5 12 13 84 85
2
"""