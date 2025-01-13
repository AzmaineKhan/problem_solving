

t=int(input())

for i in range(t):
    n= int(input())
    for j in range(n):
        print("*",end='')
        for k in range(n-1):
            print("*",end='')
        print()
    print()