






def multiply(a,b):
    #a*b = a+b(a-1)
    max1 = max(a,b)
    min1 = min(a,b)
    if min1==1:
        return max1
    return max1+multiply(max1,min1-1)

if __name__ == '__main__':

    print(multiply(3,4))
    