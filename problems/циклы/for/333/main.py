first_number = int(input())
second_number = int(input())
for item in range(first_number, second_number + 1):
    if item % 2 == 0:
        print(item, end=" ")