with open("241.txt") as f:
    s = f.readline()
    s = s.replace("11A", "*")
    s = s.replace("11B", "*")
    s = s.replace("12A", "*")
    s = s.replace("12B", "*")
    s = s.replace("21A", "*")
    s = s.replace("21B", "*")
    s = s.replace("22A", "*")
    s = s.replace("22B", "*")
    count = 0
    b = []
    for i in s:
        if i == "*":
            count += 1
        else:
            b.append(count)
            count = 0
    print(max(b))







        
    
    