#https://kompege.ru/variant?kim=25013947
for x in {0,1}:
    for y in {0,1}:
        for z in {0,1}:
            for w in {0,1}:
                F = (not(not(x) or z) or y) or not(w)
                if F == 0:
                    print(x,y,z,w)