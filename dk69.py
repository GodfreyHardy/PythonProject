




def generate(lt,sign,res,begin,s):
    if begin == 7:
        res.append(s)
    for i in range(4):
        if sign[i] == 0:
            sign[i] = 1
            if begin==0 or begin==2 or begin==4:
                for j in range(4):
                    if j==0:
                        generate(lt,sign,res,begin+2,s+str(lt[i])+'+')
                    elif j==1:
                        generate(lt, sign, res, begin + 2, s + str(lt[i]) + '-')
                    elif j==2:
                        generate(lt, sign, res, begin + 2, s + str(lt[i]) + '*')
                    elif j==3:
                        generate(lt, sign, res, begin + 2, s + str(lt[i]) + '//')
            elif begin==6:
                generate(lt,sign,res,begin+1,s+str(lt[i]))
            sign[i] = 0
    return res

def cal(s):
    s = s.replace('//', '/')
    op = []
    d = []
    i = 0
    while i < len(s):
        tmp1 = ''
        while i<len(s) and ord('0')<=ord(s[i])<=ord('9'):
            tmp1 += s[i]
            i += 1
        d.append(int(tmp1))
        if i<len(s):
            op.append(s[i])
        i += 1
    while len(d)>0 and len(op)>0:
        d1 = d.pop(0)
        d2 = d.pop(0)
        k = op.pop(0)
        d3 = 0
        if k=='+':
            d3 = d1 + d2
        elif k=='-':
            d3 = d1 - d2
        elif k=='*':
            d3 = d2 * d1
        elif k=='/':
            d3 = d1 // d2
        d.insert(0,d3)
    #print(d)
    return d[0]

def printcmp(s):
    s = s.replace('11', 'J')
    s = s.replace('12', 'Q')
    s = s.replace('13', 'K')
    s = s.replace('1', 'A')
    s = s.replace('//', '/')
    print(s)
# 二十四点运算
if __name__ == '__main__':
    s = input().split(' ')
    lt = []
    flag = 0
    for i in range(len(s)):
        if s[i] == 'joker' or s[i] == 'JOKER':
            print('ERROR')
            flag = 1
            break
        if s[i] == 'J':
            lt.append(11)
        elif s[i] == 'Q':
            lt.append(12)
        elif s[i] == 'K':
            lt.append(13)
        elif s[i] == 'A':
            lt.append(1)
        else:
            lt.append(int(s[i]))
    if not flag:
        # eval
        sign = [0]*4
        s = generate(lt,sign,[],0,'')
        #print(s)
        print(len(s))
        flag = 0
        for i in range(len(s)):
            if cal(s[i]) == 24:
                printcmp(s[i])
                flag = 1
                break
        if flag == 0:
            print('NONE')