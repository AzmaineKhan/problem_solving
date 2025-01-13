

t = int(input())
for i in range(t):
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    if( n1 > n2 and n2 > n3):
        temp = n1
        n1 = n3
        n3 = temp
    if(n2 > n1 and n2 > n3 and n3 > n1):
        temp = n2
        n2 = n3
        n3 = temp
    if(n1 > n2 and n1 > n3 and n3 > n2):
        temp = n1
        n1 = n2
        n2 = n3
        n3 = temp

    if(n1 > n2 and n3 > n1):
        temp = n1
        n1 = n2
        n2 = temp
    print("Case ",i+1,": ",n1," ",n2," ",n3, sep="")


