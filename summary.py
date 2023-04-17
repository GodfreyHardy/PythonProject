





if __name__ == '__main__':
    lt = []
    for i in range(100):
        s = input()
        if len(s)==0:
            break
        s = s.split('.')
        lt.append(str(i+1)+'.'+s[1])
    for item in lt:
        print(item)