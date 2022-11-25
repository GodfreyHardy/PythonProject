"""
■ 题目描述
某个打印机根据打印队列执行打印任务。打印任务分为九个优先级，分别用数字1-9表示，数字越大优先级越高。打印机每次从队列头部取出第一个任务A，
然后检查队列余下任务中有没有比A优先级更高的任务，如果有比A优先级高的任务，则将任务A放到队列尾部，否则就执行任务A的打印。
请编写一个程序，根据输入的打印队列，输出实际的打印顺序。
输入描述
输入一行，为每个任务的优先级，优先级之间用逗号隔开，优先级取值范围是1~9。
输出描述
输出一行，为每个任务的打印顺序，打印顺序从0开始，用逗号隔开
示例 1 输入输出示例仅供调试，后台判题数据一般不包含示例
输入
9,3,5
输出
0,2,1
说明
队列头部任务的优先级为9，最先打印，故序号为0；
接着队列头部任务优先级为3，队列中还有优先级为5的任务，优先级3任务被移到队列尾部；
接着打印优先级为5的任务，故其序号为1；
最后优先级为3的任务的序号为2。
"""

if __name__ == '__main__':
    s = input()
    s = s.split(',')
    lt = sorted(s,reverse=True)
    dic = {}
    for i in range(len(lt)):
        if int(lt[i]) not in dic:
            dic[int(lt[i])] = [i]
        else:
            dic[int(lt[i])].append(i)
    print(lt)
    #a = sorted(dic.items(),key=lambda x:(x[1],-x[0]),reverse=True)
    #print(a)
    res = ""
    for i in range(len(s)):
        j = 0
        while dic[int(s[i])][j]==-1:
            j += 1
        res += str(dic[int(s[i])][j])+','
        dic[int(s[i])][j] = -1
    res = res[0:len(res)-1]
    print(res)