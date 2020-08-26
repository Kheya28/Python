
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

p=fact(4)
print(p)