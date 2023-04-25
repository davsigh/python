print("Welcome to passowrd generator program")
import string
import random
letters = ["a", "b", "c", "d", "e", "f"]
numbers = ["0", "1", "2", "3", "4" "5"]
symbols = ["!", "@", "#", "$", "%"]
total_letter = int(input("How many letters you like password"))
total_symbol = int(input("how many symbols you want in password"))
total_number = int(input("how many numbers you want in password"))
# for a in string.ascii_lowercase:
#     print (a)
# password = ""
# for a in range(1, total_letter + 1 ):
#     password += random.choice(letters)
# #print(password)
# for b in range(1, total_number + 1):
#     password += random.choice(numbers)
# #print(password)
# for c in range(1, total_symbol + 1):
#     password+= random.choice(symbols)
# print(password)    

######  Hard Password ########
password_list = letters + symbols + numbers
password=""
for a in range(1, total_letter + 1 ):
    password += random.choice(password_list)
#print(password)
for b in range(1, total_number + 1):
    password += random.choice(password_list)
#print(password)
for c in range(1, total_symbol + 1):
    password+= random.choice(password_list)
print(password) 
random.shuffle(password)
print(password)