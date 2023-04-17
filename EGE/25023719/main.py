#https://kompege.ru/variant?kim=25023719
a = [0] * 2030
for i in range(2025, 2030):
    a[i] = i
for i in range(2024,-1,-1):
    a[i] = i + a[i + 2]
    
print(a[2022] - a[2023])
    