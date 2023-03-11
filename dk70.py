



"""
[24点游戏]
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,
除法指实数除法运算,运算符仅允许出现在两个数字之间,本题对数字
选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，
但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
"""


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
                        generate(lt, sign, res, begin + 2, s + str(lt[i]) + '/')
            elif begin==6:
                generate(lt,sign,res,begin+1,s+str(lt[i]))
            sign[i] = 0
    return res



if __name__ == '__main__':
    s = input().split(' ')
    lt = []
    for i in range(len(s)):
        lt.append(int(s[i]))
    sign = [0] * 4
    s = generate(lt, sign, [], 0, '')
    flag = 0
    # print(s)
    for item in s:
        k = []
        i = 0
        #print(item)
        while i < len(item):
            s2 = ''
            while i<len(item) and ord('0')<= ord(item[i])<=ord('9'):
                s2 += item[i]
                i += 1
            k.append(s2)
            if i<len(item):
                k.append(item[i])
            i += 1
        #添加括号
        for i in range(4):#0 2 4 6
            for j in range(i * 2 + 2, 7, 2):
                k2 = []
                k2.extend(k)
                k2.insert(2*i,'(')
                k2.insert(j+2,')')
                s4 = ''
                for i2 in range(2*i,j+2+1):
                    s4 += k2[i2]
                if eval(s4)==0 or eval(s4)==0.0:
                    continue
                s3 = ''
                for sitem in k2:
                    s3 += sitem
                #print(s3)
                if eval(s3)==24.0 or eval(s3)==24:
                    print('true')
                    flag = 1
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        print('false')
    # for i in range(4):  # 0 2 4 6
    #     print(str(i))
    #     for j in range(i * 2 + 2, 7, 2):
    #         print(j)

