x_number = int(input())
for item in range(1, x_number + 1):
    if x_number % item == 0:
        print(item, end=" ")
        