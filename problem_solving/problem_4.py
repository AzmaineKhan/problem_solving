

test=int(input())
for i in range(test):
    n = int(input())
    print("Case ",i+1,": ",sep="",end="")
    for j in range(1, n+1):
        if n % j== 0:
            print(j, end=' ')
    print()