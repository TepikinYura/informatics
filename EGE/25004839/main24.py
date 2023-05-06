with open ("24.txt", "r") as f:
    lines = f.readlines()
    a = []
    for i in lines[0]:
        a.append(i)
count = 0
max_num = 0
for i in range(len(a) - 1):
    if a[i] + a[i +1] != "PP":
        count += 1
        if max_num < count:
            max_num = count
    else:
        count = 0
print(max_num)