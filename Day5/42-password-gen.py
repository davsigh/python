import string
import random

print("Welcome to password generator program")

letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list("!@#$%")

total_letter = int(input("How many letters do you want in your password? "))
total_symbol = int(input("How many symbols do you want in your password? "))
total_number = int(input("How many numbers do you want in your password? "))

password_list = []
for i in range(total_letter):
    password_list.append(random.choice(letters))

for i in range(total_symbol):
    password_list.append(random.choice(symbols))

for i in range(total_number):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
password = "".join(password_list)
print(password)
