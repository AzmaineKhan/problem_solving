#This program finds out a grade from your marks


num = int(input("Enter Your Marks: "))

# if  num >= 80 and num <= 100:
#     print("A+")
# elif num >= 70 and num <= 79:
#     print("A")
# elif num >= 60 and num <= 69:
#     print("B")
# elif num >= 50 and num <= 59:
#     print("C")
# elif num >= 40 and num <= 49:
#     print("D")
# else:
#     print("F")


if num < 0 or num > 100:
    print("Please Enter a valid number!!")

else:
    if  num >= 80:
        print("A+")
    elif num >= 70:
        print("A")
    elif num >= 60:
        print("B")
    elif num >= 50:
        print("C")
    elif num >= 40:
        print("D")
    else:
        print("F")
    print("The program was successfully ran!!")    

