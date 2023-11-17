a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

num = int(input("Enter a number: "))

for element in a:
    if element < num:
        b.append(element)

print(b)