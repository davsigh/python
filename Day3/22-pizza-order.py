print("Welcome to Pizza Shop")
size = input("What size pizza do you want ? S,M,L ")
add_peproni = input("Do you want to add peproni Y or N ")
extra_cheese = input("Do you want to add extra cheese ? Y or N ")
if size == "S":
    print("You have ordered Small pizza")
    cost = 15
if size == "M":
    print("You have ordered Medium pizza")
    cost = 20
else:
    print("not ordered Medium")
if size == "L":
    print("You have ordered Large pizza")
    cost = 25
if add_peproni == "Y":
    cost += 2
    print("Added the peproni cost in pizza")
if extra_cheese == "Y":
    cost += 3
    print("added extra cheese cost in pizza")
print("total bill is ", cost)



