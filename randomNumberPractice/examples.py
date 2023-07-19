#example code from lecturer
import random

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the die...")

    die_value = (random.randint(min,max))

    print("The value is: ", die_value)

    if die_value == 1:
        print("Answer number one")

    elif die_value == 2:
        print("Answer number 2")

    elif die_value == 3:
        print("Answer number 3")
    
    elif die_value == 4:
        print("Answer number 4")

    elif die_value == 5:
        print("Answer number 5")
    
    else:
        print("Answer number 6")

    roll_again = input("Roll again?")