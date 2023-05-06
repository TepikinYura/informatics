def f(s):
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    return n
        
for i in range(520,1000):
    print(f(i))
    if f(i) == 64:
        print(i)