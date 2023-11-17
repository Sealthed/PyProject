num = int(input("Enter a number: "))

x = list(range(1, num))
y = []

for element in x:
    if num % element == 0:
        y.append(element)

print(y)