
"""
■ 题目描述
【货币单位换算】
记账本上记录了若干条多国货币金额，需要转换成人民币分（fen），汇总后输出。
每行记录一条金额，金额带有货币单位，格式为数字+单位，可能是单独元，或者单独分，或者元与分的组合。
要求将这些货币全部换算成人民币分（fen）后进行汇总，汇总结果仅保留整数，小数部分舍弃。
元和分的换算关系都是1:100，如下：
1CNY=100fen（1元=100分）
1HKD=100cents（1港元=100港分）
1JPY=100sen（1日元=100仙）
1EUR=100eurocents（1欧元=100欧分）
1GBP=100pence（1英镑=100便士）
汇率如下表：
CNY JPY HKD EUR GBP
100 1825 123 14 12
即100CNY=1825JPY=123HKD=14EUR=12GBP
输入描述
第一行输入为N，N表示记录数。0<N<100
之后N行，每行表示一条货币记录，且该行只会是一种货币。
输出描述
将每行货币转换成人民币分（fen）后汇总求和，只保留整数部分。
输出格式只有整数数字，不带小数，不带单位。
示例1
输入
1
100CNY
输出
10000
示例2
输入
1
3000fen
输出
3000
示例3
输入
1
123HKD
输出
10000
示例4
输入
2
20CNY53fen
53HKD87cents
输出
6432
解题思路
可以根据每种货币的首字母来区分货币类型，注意元和分都存在情况的处理。
"""


if __name__ == '__main__':
    n = int(input())
    res = 0
    for i in range(n):
        s = input()
        j = 0
        while j < len(s):
            tmp = ''
            while j<len(s) and ord('0') <= ord(s[j])<=ord('9'):
                tmp += s[j]
                j += 1
            #CNY JPY HKD EUR GBP
            #100 1825 123 14 12
            """
            1CNY=100fen（1元=100分）
            1HKD=100cents（1港元=100港分）
            1JPY=100sen（1日元=100仙）
            1EUR=100eurocents（1欧元=100欧分）
            1GBP=100pence（1英镑=100便士）
            """
            if s[j]=='C':
                res += int(tmp)*100
                j += 3
            elif s[j]=='H':
                res += int(tmp)/123*10000
                j += 3
            elif s[j]=='J':
                res += int(tmp)/1825*10000
                j += 3
            elif s[j]=='E':
                res += int(tmp)/14*10000
                j += 3
            elif s[j]=='G':
                res += int(tmp)/12*10000
                j += 3
            elif s[j]=='f':
                res += int(tmp)
                j += 3
            elif s[j]=='c':
                res += int(tmp)/123*100
                j += 5
            elif s[j]=='s':
                res += int(tmp)/1825*100
                j += 3
            elif s[j]=='e':
                res += int(tmp)/14*100
                j += 9
            elif s[j]=='p':
                res += int(tmp)/12*100
                j += 5
            #print(res)
    #print(eval('2053+53/123*10000+87/123*100'))
    #print(res)
    print(int(res))