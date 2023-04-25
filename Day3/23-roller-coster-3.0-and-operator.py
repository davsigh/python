print("Welcome to roller coaster ride")
height = float(input("Please enter your height in cm "))

print(height)
print(type(height))

if height > 100:
    print("you can take this ride")
    age = int(input("Enter your age "))
    print(type(int(age)))
    if age < 12:
        bill = 10
        print("ticket price is 10$")
    elif age < 18 and age > 12:
        bill = 12
        print ("Tickets price is 12$") 
    elif age >=18 and age < 45 or age > 55:
        bill = 15
        print("Ticket price is 15$")
    elif age > 45 and age < 55:
        bill = 0
        print("ticket is free for your age") 
    photo = input("Do you want photo? please write yes or no ")
    if photo == "yes":
        print("Add 3$ in bill")
        bill += 3
        print(f"total bill is ",bill)
else:
  print("you can't")