

t=int(input())
for i in range(t):
    n=int(input())
    mul=1
    for j in range(2, n+1):
        mul = mul*j
    print(mul)