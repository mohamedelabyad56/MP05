print("Welcome to Treasure Island! Your Mission is to find the treasure.")
pr1 = input("Left or right? ").lower()  # Convert input to lowercase for consistency

if pr1 == "right":
    print("You fell into a hole. Game Over.")
elif pr1 == "left":
    pr2 = input("Swim or wait? ").lower()
    
    if pr2 == "swim":
        print("Attacked by trout. Game Over.")
    elif pr2 == "wait":
        pr3 = input("Which door? (blue/red/yellow) ").lower()
        
        if pr3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif pr3 == "red":
            print("Burned by fire. Game Over.")
        elif pr3 == "yellow":
            print("You win!")
        else:
            print("Game Over. You chose an invalid door.")
else:
    print("Game Over. You chose an invalid direction.")

