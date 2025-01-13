

t=int(input())
if t<= 100:
    for i in range(t):
        n=int(input())
        if 1 <= n <= 120:
            num_of_0 = 0
            while n >=5:
                n=n // 5
                num_of_0 = num_of_0 + n 
            print(num_of_0)    


