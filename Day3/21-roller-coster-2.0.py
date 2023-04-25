print("Welcome to roller coaster ride")
height = float(input("Please enter your height in cm "))

print(height)
print(type(height))

if height > 100:
    print("you can take this ride")
    age = int(input("Enter your age "))
    photo = input("Do you want photo? please write yes or no ")
    print(type(int(age)))
    if photo == "yes":
        print("will add 3$ in your bill")
    if age < 12:
        if photo == "yes":
            print("your ticket price is 13$ with photo")
        else:
            print("ticket price is 10$")
    elif age < 18:
        if photo == "yes":
            print("your ticket price is 15$ with photo")
        else:
            print ("Tickets price is 12$") 
    elif age >=18:
        if photo == "yes":
            print("your ticket price is 18$ with photo")
        else:
            print("Ticket price is 15$")
else:
    print("you can't")