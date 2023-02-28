

"""
■ 题目描述
【数组中心位置】
2 3 5 5 5 6
"""

def cmp(left,right):
    for i in range(2,11):
        if left[i] != right[i]:
            return False
    return True

if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    lt = []
    if len(lt)==1:
        print(0)
    else:
        right = [0] * 11
        for i in range(len(s)):
            lt.append(int(s[i]))
            if i > 0:
                if lt[i]==10:
                    right[2] += 1
                    right[5] += 1
                elif lt[i]==9:
                    right[3] += 2
                elif lt[i]==8:
                    right[2] += 3
                elif lt[i]==6:
                    right[2] += 1
                    right[3] += 1
                elif lt[i]==4:
                    right[2] += 2
                else:
                    right[lt[i]] += 1
        if right[1] == len(s)-1:
            print(0)
        else:
            left = [0] * 11
            flag = 0
            for i in range(1,len(lt)):
                if lt[i-1] == 10:
                    left[2] += 1
                    left[5] += 1
                elif lt[i-1] == 9:
                    left[3] += 2
                elif lt[i-1] == 8:
                    left[2] += 3
                elif lt[i-1] == 6:
                    left[2] += 1
                    left[3] += 1
                elif lt[i-1] == 4:
                    left[2] += 2
                else:
                    left[lt[i-1]] += 1
                if lt[i] == 10:
                    right[2] -= 1
                    right[5] -= 1
                elif lt[i] == 9:
                    right[3] -= 2
                elif lt[i] == 8:
                    right[2] -= 3
                elif lt[i] == 6:
                    right[2] -= 1
                    right[3] -= 1
                elif lt[i] == 4:
                    right[2] -= 2
                else:
                    right[lt[i]] -= 1
                print(left)
                print(right)
                if cmp(left,right):
                    flag = 1
                    print(i)
                    break
            if flag == 0:
                print(-1)
