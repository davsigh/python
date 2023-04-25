# print("Welcome to roller coaster ride")
# height = float(input("Please enter your height in cm "))

# print(height)
# print(type(height))

# if height > 100:
#     print("you can take this ride")
#     age = int(input("Enter your age "))
#     print(type(int(age)))
#     if age <= 18:
#         print("ticket price is 10$")
#     else:
#         print("Ticket price is 15$")
# else:
#     print("you can't")
######## Working above code ###########
print("Welcome to roller coaster ride")
height = float(input("Please enter your height in cm "))

print(height)
print(type(height))

if height > 100:
    print("you can take this ride")
    age = int(input("Enter your age "))
    print(type(int(age)))
    if age <= 18 and age >12:
        print("ticket price is 12$")
    elif age <= 12:
        print ("Tickets price is 10$") 
    else:
        print("Ticket price is 15$")
else:
    print("you can't")