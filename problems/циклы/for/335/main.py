a_number = int(input())
b_number = int(input())
for item in range(a_number, b_number + 1):
    if int(item ** 0.5) ** 2 == item:
        print(item, end=" ")