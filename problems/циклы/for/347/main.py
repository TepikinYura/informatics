N_number = int(input())
count = 0
for item in range(1, N_number + 1):
    item = int(input())
    if item == 0:
        count += 1
if count != 0:
    print("YES")
else:
    print("NO")