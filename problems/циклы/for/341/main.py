x_number = int(input())
count = 0
for item in range(1, x_number + 1):
    if x_number % item == 0:
        count += 1
print(count)