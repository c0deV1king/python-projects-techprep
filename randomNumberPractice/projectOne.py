#importing the random module
import random
#setting the minimum and max amount for the random generator
min = 1
max = 9
#Default input to yes until user specifies no
ask_question = "yes"
#while loop containing the game
while ask_question == "yes" :
    ask_question = input("What would you like to ask? ")
    #Using random module to choose a random number
    questionAnswer = (random.randint(min,max))
    #Possible answers to the question the user inputs
    if questionAnswer == 1:
        print("You may rely on it.")

    elif questionAnswer == 2:
        print("Most likely")

    elif questionAnswer == 3:
        print("As I see it, yes.")

    elif questionAnswer == 4:
        print("Very doubtful.")

    elif questionAnswer == 5:
        print("MY sources say no.")

    elif questionAnswer == 6:
        print("Don't count on it.")

    elif questionAnswer == 7:
        print("Ask again later.")

    elif questionAnswer == 8:
        print("Couldn't tell ya.")
    #needs to end in else to move on
    else:
        print("I couldn't hear you.")

    #asking the user if they want another go, replying no will exit
    ask_question = input("Would you like to ask another question? ")
