
if __name__ == '__main__':
    s = input()
    res = ""
    num = []
    alpha = []
    symbol = []
    i = 0
    pre = ""
    while i < len(s):
        if ord('a')<=ord(s[i])<=ord('z'):
            tmp = ""
            while ord('a')<=ord(s[i])<=ord('z'):
                tmp += s[i]
                i += 1
            alpha.append(tmp)
        elif ord('0')<=ord(s[i])<=ord('9'):
            k = ""
            while ord('0')<=ord(s[i])<=ord('9'):
                k += s[i]
                i += 1
            k = int(k)
            num.append(k)
        elif s[i] == '[':
            symbol.append(s[i])
            i += 1
        elif s[i] == ']':
            letter = alpha.pop()
            k = num.pop()
            symbol.pop()
            tmp = ""
            letter += pre
            for j in range(k):
                tmp += letter
            pre = tmp
            i += 1
            if len(symbol) == 0:
                pre = ""
                res += tmp
    print(res)
    print(len(res))