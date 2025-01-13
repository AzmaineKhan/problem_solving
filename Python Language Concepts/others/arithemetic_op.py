# write code to  add, subtrac, multiply, division of two numbers
"""
Ref:
Addition +
substraction -
multiplication *
division /
modulus(Remider) %

"""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

sum = a + b
sub = a - b
mul = a * b
div = a // b
mod = a % b



print(f"Sum of {a} + {b} = {sum}")
print(f"substraction of {a} - {b} = {sub}")
print(f"multiplication of {a} * {b} = {mul}")
print(f"{a} Divided by {b} = {div}")
print(f"Mod of {a} % {b} = {mod}")

print(type(sum))
print(type(sub))
print(type(mul))
print(type(div))
print(type(mod))
