# This is the Python file for the Week 2
import random
choices=["Rock","Paper","Scissors"]
print(choices)
playChoice = int(input("Enter your choice (1.Rock, 2.Paper, 3.Scissors): "))
print(playChoice)
if playChoice < 1 or playChoice > 3:
    print("Error: Choice must be between 1 and 3!")
else:
    computerChoice=random.randint(1,3)

    playChoiceIndex=choices[playChoice-1]
    computerChoiceIndex=choices[computerChoice-1]

    print("You chose: ", playChoiceIndex)
    print("Computer chose: ", computerChoiceIndex)

    # Determine the winner using if/ilif/else
    if playChoiceIndex ==computerChoiceIndex:
        print("It is a tie!")
    elif playChoiceIndex == 0 and computerChoiceIndex ==2:
        print("Rock beats Rock - You win!")
    elif playChoiceIndex == 1 and computerChoiceIndex ==0:
        print("Paper beats Rock - You win!")     
    elif playChoiceIndex == 2 and computerChoiceIndex ==1:
        print("Scissor beats Rock - You win!")   
    else:
        print("You lose!")
        

