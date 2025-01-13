

for i in range(100):
    num = int(input("Enter an even number: "))
    if num % 2 == 0:
        print("The loop is running")
    else:
        break
print("The loop is terminated")