sample = str(input("Enter a word: "))

a = str(sample)
b = sample[::-1]

if a == b:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")


