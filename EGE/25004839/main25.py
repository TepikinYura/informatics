def find_M(x):
    for i in range(2,x//2):
        if x % i == 0:
            min_divisor = i
            break
        else:
            min_divisor = 0
    for i in range(x-1,2,-1):
        if x % i == 0:
            Max = i
            break
        else:
            Max = 0
    M = min_divisor + Max
    return str(M)
print(find_M(25))
count = 0
for i in range(700001,800000):
    if find_M(i)[len(find_M(i)) - 1] == "8":
        if count < 5:
            count +=1
            print(i, find_M(i))
        else:
            break
    