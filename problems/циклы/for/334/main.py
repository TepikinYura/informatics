a_number = int(input())
b_number = int(input())
c_number = int(input())
d_number = int(input())
for item in range(a_number, b_number + 1):
    if item % d_number == c_number:
        print(item, end=" ")
