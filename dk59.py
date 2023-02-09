
"""
第二道是先给定一个字符串序列第一个字符串R第二个字符串就是BR第三个字符串就是RBBR
就是第i个字符串等于第i-1个字符串取反加上第i-1个字符串：B取反就是R
只有这两个字符然后他输入第几个字符串的第几个字符让你输出R输出red B输出blue
"""
#
def generate(n):
    if n==1:
        return '1'
    s = generate(n-1)
    pre = ''
    for i in range(len(s)):
        if s[i] == '1':
            pre += '0'
        else:
            pre += '1'
    return pre + s


#0 10 0110 10010110
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    k = generate(n)
    print(len(k))
    print(k[m-1])
