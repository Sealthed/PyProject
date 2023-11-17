num1 = int(input("Enter a number: "))

modcal = num1 % 2
mod4 = num1 % 4

if mod4 == 0:
    print("The number is a multiple of 4")
elif modcal == 0:
    print("The number is even")
else:
    print("The number is odd")