# Password-Generator
Python code for password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_']

charNo = int(input("Enter the number of characters you want the password to be: "))
symNo = int(input("How many symbols would you like in your password: "))
numNo = int(input("How many numbers would you like in your password: "))

chr1 = 0
sym1 = 0
num1 = 0

password = ''
for i in range(1, charNo+symNo+numNo+1):
    x = random.randint(1, 3)
    if x == 1 and chr1 < charNo:
        password += letters[random.randint(0, len(letters) - 1)]
        chr1 += 1
    elif x == 2 and sym1 < symNo:
        password += symbols[random.randint(0, len(symbols) - 1)]
        sym1 += 1
    elif x == 3 and num1 < numNo:
        password += str(numbers[random.randint(0, 9)])
        num1 += 1
    elif chr1 < charNo:
        password += letters[random.randint(0, len(letters) - 1)]
        chr1 += 1
    elif num1 < numNo:
        password += str(numbers[random.randint(0, 9)])
        num1 += 1
    elif sym1 < symNo:
        password += symbols[random.randint(0, len(symbols) - 1)]
        sym1 += 1
print(f"The generated password is: {password}")
