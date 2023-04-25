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
    elif age < 18:
        bill = 12
        print ("Tickets price is 12$") 
    elif age >=18:
        bill = 15
        print("Ticket price is 15$")
else:
    print("you can't")
photo = input("Do you want photo? please write yes or no ")
if photo == "yes":
    print("Add 3$ in bill")
    bill += 3
    print(f"total bill is ",bill)