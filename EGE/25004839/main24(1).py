with open("24.txt", "r") as f:
    s = f.readline()
    print(s[:10])
    a = s.split("PP")
    length = []
    for i in a:
        length.append(len(i))
        
    print(max(length), length)
