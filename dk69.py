




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

# 二十四点运算
if __name__ == '__main__':
    s = input().split(' ')
    lt = []
    for i in range(len(s)):
        if s[i] == 'joker' or s[i] == 'JOKER':
            print('ERROR')
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
    # eval
    sign = [0]*4
    s = generate(lt,sign,[],0,'')
    #print(s)
    print(len(s))
    flag = 0
    for i in range(len(s)):
        if eval(s[i]) == 24:
            print(s[i])
            flag = 1
            break
    if flag == 0:
        print('NONE')