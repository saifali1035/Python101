#Importing random to use random fuction for computer to enter its value in the game.
import random

#this function helps us to print the user's choice in the game.
def game_keywords(word):
    if word=='s':
        print("Snake")
    if word=='w':
        print("Water")
    if word=='g':
        print("Gun")


#Banner Can be modeified to your liking
print('''         Hello User Welcome to the GAME !!!
         Computer has chosen its option
         Now its your turn !!!''')

#Taking user input
user_choice=input("Enter your choice : Snake(s), Water(w) or Gun(g) :")

#Generating Random number between 1, 2 and 3 for computer input in the game.
random_choice_for_comp_int=random.randint(1,3)

#Converting random number to a choice valid in game
if random_choice_for_comp_int==1:
    computer_choice='s'
elif random_choice_for_comp_int==2:
    computer_choice='w'
elif random_choice_for_comp_int==3:
    computer_choice='g'

#Game Logic (Snake wins over Water , Gun win over Snake and Water wins over Gun.)
if computer_choice==user_choice:
    print("Match Draw ! You both choose", game_keywords(computer_choice) )
elif computer_choice=='s' and user_choice=='w':
    print("You Lost !  As Computer Choose Snake !")
elif computer_choice=='s' and user_choice=='g':
    print("You Won !   As Computer Choose Snake !")
elif computer_choice=='w' and user_choice=='s':
    print("You Won !   As Computer Choose Water !")
elif computer_choice=='w' and user_choice=='g':
    print('You Lost !  As Computer Choose Water !')
elif computer_choice=='g' and user_choice=='s':
    print('You Lost !  As Computer Choose Gun !')
elif computer_choice=='g' and user_choice=='w':
    print('You Won !   As Computer Choose Gun !')
else:
    print("Invalid Choice ! ")


