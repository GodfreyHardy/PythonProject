
"""
input:
abcdefg 3
output:
afg
be
cd
"""
if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    n = int(s[1])
    s = s[0]
    m = (len(s)//n) + 1
    lt = [['-']*m for _ in range(n)]
    row = 0
    col = 0
    diff = 1
    for i in range(len(s)):
        lt[row][col] = s[i]
        if (i+1) % n == 0:
            diff *= -1
            col += 1
        else:
            row += diff
    for i in range(n):
        res = ''
        for j in range(m):
            if lt[i][j] != '-':
                res += lt[i][j]
        if res != '':
            print(res)
