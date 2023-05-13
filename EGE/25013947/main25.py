s = "123"
s_2 = "890"
for i in range(100):
    string = s + str(i) + s_2
    if int(string) % 27 == 0:
        print(string, int(string) // 27)