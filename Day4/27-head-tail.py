import random
print("Lets have challenge of Head & Tail")
choice = input("Head or tail? ")
num = random.randint(0,1)
if num == 0:
    print("Head")
else:
    print("Tail")
