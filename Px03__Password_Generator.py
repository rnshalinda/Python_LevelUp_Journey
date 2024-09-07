# Random Pass word genarator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

let = int(input("How many letters would you like in your password? ->>"))
sym = int(input("How many symbols would you like? ->>"))
num = int(input("How many numbers would you like? ->>"))

array = [letters, symbols, numbers]

a = []
b = []

for i in range(0, let):
    a += random.choice(letters)

for i in range(0, sym):
    a += random.choice(symbols)

for i in range(0, num):
    a += random.choice(numbers)

print(f"\nBefore random mix : {a}\n")

for i in a:
    random_place = random.randint(0, len(a))
    b.insert(random_place, i)

print(f"Password : {''.join(b)}") #concatenate list

# Easier methode to randomize pswd
random.shuffle(a)
print(f"other option : {''.join(a)}")