#https://vk.com/away.php?to=https%3A%2F%2Finf-ege.sdamgia.ru%2Fproblem%3Fid%3D15618&cc_key=
for w in {0,1}:
    for x in {0,1}:
        for y in {0,1}:
            for z in {0,1}:
                F = (x and not(y)) or (y == z) or not(w)
                if F == 0:
                    print(w,x,y,z)
                    break
#Ответ wzyx