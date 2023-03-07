x_number = int(input())
for item in range(2, x_number + 1):
    if x_number % item == 0:
        print(item)
        break