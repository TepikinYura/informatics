with open ("26.txt","r") as f:
    S,N = f.readline().split()
    a = []
    for i in range(int(N)):
        num = int(f.readline())
        a.append(num)
        
    a.sort()
    b = []
    
    for i in range(int(N)):
        if sum(b) + a[i] <= int(S):
            b.append(a[i])
        else:
            break
    
    b[-1] = 0
    print(sum(b))
    for i in range(int(N) - 1,-1,-1):
        if int(S) - sum(b) >= a[i]:
            b[-1] = a[i]
            break
    print(b[-1], len(b))