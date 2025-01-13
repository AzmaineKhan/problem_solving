

rep = int(input("How many digits do you want to check: "))

for i in range(0, rep, 2):
    print(f"i = {i}")
    num = int(input("Enter the value: "))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")