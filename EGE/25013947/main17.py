#https://kompege.ru/variant?kim=25013947
with open("171.txt","r") as f:
    lines = f.readlines()
    a = []
    for i in lines:
        a.append(int(i))
    print(a)
    min_num = min(a)
    b = []
    for i in range(len(a) - 1):
        if a[i] % 117 == min_num or a[i + 1] % 117 == min_num:
                b.append(a[i] + a[i + 1])
    print(len(b), max(b), min_num)