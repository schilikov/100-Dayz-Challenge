# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Not randomised order of password chars.
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass_ordered = ""

for let in range(0, nr_letters):
    pass_ordered += random.choice(letters)

for sym in range(0, nr_symbols):
    pass_ordered += random.choice(symbols)

for num in range(0, nr_numbers):
    pass_ordered += random.choice(numbers)

print(f"This is your random password in order: {pass_ordered}")

# Randomised order of password chars.
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_not_ordered = []

for let in range(0, nr_letters):
    pass_not_ordered.append(random.choice(letters))

for sym in range(0, nr_symbols):
    pass_not_ordered.append(random.choice(symbols))

for num in range(0, nr_numbers):
    pass_not_ordered.append(random.choice(numbers))

random.shuffle(pass_not_ordered)
new_pass = ''.join(pass_not_ordered)

print(f"This is your random password not in order: {new_pass}")