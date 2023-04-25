print("Welcome to Treasure Island Game")
dir = input("Do you want to take left or right ").lower()
print(dir)
if dir == "right":
    print ("Game Over for you")
elif dir == "left":
    print("Lets go to next stage")
    game = input("You have river infront of you. Do you want to wait or swim? ").lower()
    if game == "swim":
        print("Game Over for you")
    else:
        print("you reached to final level")
        door = input("There are three doors which one do you want to choose(Red,blue or green ) ?").lower()
        if door == "green":
            print("you Won!")
        elif door == "red":
            print("There is lion and you lost the game")
        else:
            print("You choose wrong door. You are dead now!")



    
