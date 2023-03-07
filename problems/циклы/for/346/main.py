count_nulls = 0
count_plus = 0
count_minus = 0
N_number = int(input())
for item in range(1, N_number + 1):
    item = int(input())
    if item == 0:
        count_nulls += 1
    elif item > 0:
        count_plus += 1
    else:
        count_minus += 1
print(count_nulls, count_plus, count_minus)