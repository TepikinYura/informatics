def max_dig(n,md=0):
    if n<10:
        return max(n,md)
    else:
        return max_dig(n//10,max(md,n%10))
        
n=int(input())
print(max_dig(n))