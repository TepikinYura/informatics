def dec_to_bin(n):
    s ="";
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
def sum_all_nums(s):
    result = 0
    for i in s:
        if i == "1":
            result += 1
    return result
for num in range(1000):
    bin_num = dec_to_bin(num)
    bin_num = bin_num + str(sum_all_nums(bin_num) % 2)
    bin_num = bin_num + str(sum_all_nums(bin_num) % 2)
    r = int(bin_num, 2)
    if r > 43:
        print(r)
        break;
