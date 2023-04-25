import random
print("Welcome to play rock paper scissor")
#my_choice = input("what is your choice? Rock, Paper or Scissor")
my_choice = input("what is your choice 0 , 1 or 2 ? Rock(0), Paper(1) or Scissor(2)")
print("you have choose ", my_choice)    
print(type(my_choice))
my_choice = int(my_choice)
computer_choice = random.randint(0,2)
print(computer_choice)
print(type(computer_choice))
if my_choice >= 3 or my_choice < 0:
    print("Please pick number from 0-2")
elif my_choice == 0 and computer_choice ==2:
    print("user wins")
elif my_choice == 2 and computer_choice == 0:
    print("User loose")
elif my_choice > computer_choice:
    print ("user won")
elif computer_choice > my_choice:
    print("computer wins")
elif my_choice == computer_choice:
    print("its draw")
else:
    print("Computer Won")

