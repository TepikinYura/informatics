count = 0
for i in "2468":
    for j in "012345678":
        for t in "012345678":
            for r in "012345678":
                for e in "0234567":
                    string = i + j + t + r + e
                    if string.count("3") == 1 or string.count("3") == 0:
                        count += 1
print(count)