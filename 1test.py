


def cal(n):

    l = str(n)
    s = []
    for i in range(len(l)):
        s.append(str(l[i]))
    k = 0 #记录轮次
    sign = [0]*len(s)
    for i in range(len(s)):
        flag = 0
        if k%2 == 0:#小红
            if i==0 and sign[0]==0:
                for y in range(1,10):
                    x = len(s)-i+1#计算数位
                    if y != x and y<int(s[i]):
                        s[i] = str(y)
                        flag = 1
                        sign[i] = 1
            elif sign[i]==0:
                for y in range(0,10):
                    x = len(s)-i+1
                    if y != x and y<int(s[i]):
                        s[i] = str(y)
                        flag = 1
                        sign[i] = 1
            if flag == 0:
                for y in range(int(s[i])+1,10):
                    x = len(s) - i + 1
                    if y != x:
                        s[i] = str(y)
                        flag = 1
                        sign[i] = 1
        else:#小紫
            if i==0 and sign[0]==0:
                for y in range(9,-1,-1):
                    x = len(s)-i+1
                    if y != x and y>int(s[i]):
                        s[i] = str(y)
                        flag = 1
                        sign[i] = 1
            elif sign[i]==0:
                for y in range(9,-1,-1):
                    x = len(s)-i+1
                    if y != x and y>int(s[i]):
                        s[i] = str(y)
                        flag = 1
                        sign[i] = 1
            if flag == 0:
                for y in range(int(s[i])-1,-1,-1):
                    x = len(s) - i + 1
                    if y != x:
                        s[i] = str(y)
                        flag = 1
                        sign[i] = 1
        k += 1
        # if flag==0:
        #     break
    s2 = ''
    for i in range(len(s)):
        s2 += str(s[i])
    print(s)
    print(int(s2))

if __name__ == '__main__':
    cal(11)
