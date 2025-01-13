import math
t=int(input())
for i in range(t):
    n=int(input())

    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        print("YES")
    else:
        print("NO")
