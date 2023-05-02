with open("17.txt", "r") as f:
    lines = f.readlines()
    a = []
    for line in lines:
        a.append(int(line))
count_pairs = 0
max_summ = -20001
for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        count_pairs += 1
        if a[i] + a[i+1] > max_summ:
            max_summ = a[i] + a[i +1]
print(count_pairs, max_summ)
