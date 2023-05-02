def f(x):
    q = 9
    l = 0
    while x >= q:
        l = l + 1
        x = x - q
    m = x
    if m < l:
        m = l
        l = x
    return ([l,m])
max_value = 0
for i in range(10000):
    if f(i)[0] == 4 and f(i)[1] == 5:
        if i > max_value:
            max_value = i
print(max_value)