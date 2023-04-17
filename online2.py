





if __name__ == '__main__':
    n = int(input())
    res = 0
    for i in range(n):
        s = input()
        j = 0
        sumitem =  0
        while j < len(s):
            tmp = ''
            while ord('0')<=ord(s[j])<=ord('9'):
                tmp += s[j]
                j += 1
            tmp =  int(tmp)
            if s[j]=='C':
                sumitem += 100*tmp
                j += 3
            elif s[j]=='J':
                sumitem += tmp/1825*100*100
                j += 3
            elif s[j] == 'H':
                sumitem += tmp / 123 * 100 * 100
                j += 3
            elif s[j] == 'E':
                sumitem += tmp / 14 * 100 * 100
                j += 3
            elif s[j] == 'G':
                sumitem += tmp / 12 * 100 * 100
                j += 3
            elif s[j] == 'f':
                sumitem += tmp
                j += 3
            elif s[j] == 'c':
                sumitem += tmp / 123 * 100
                j += 5
            elif s[j] == 's':
                sumitem += tmp / 1825 * 100
                j += 3
            elif s[j] == 'e':
                sumitem += tmp / 14 * 100
                j += 9
            elif s[j] == 'p':
                sumitem += tmp / 12 * 100
                j += 5
        res += sumitem
    print(int(res))