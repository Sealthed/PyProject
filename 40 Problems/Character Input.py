name = str(input("What's your name: "))
age = int(input("How old are you: "))

old_age = 100 - age

if old_age <= 0:
    print("You are already 100 years old or even older!")
else:
    print("You will be 100 years old in " + str(old_age) + " years!")

    