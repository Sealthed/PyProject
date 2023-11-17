import random

a = []
for i in range (0, random.randint(2,10)):
    n = random.randint(1, 100)
    a.append(n)

print(a)
b = []

for element in a:
    if element % 2 == 0:
        b.append(element)

print(b)