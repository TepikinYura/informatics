number = int(input())
i = 0
while i <= number:
    if int(i ** 0.5) ** 2 == i and i != 0:
        print(i)
    i += 1