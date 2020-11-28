#Rock Paper Scissors
import random
computer_choice = random.randint(1,4)
print('Choose Rock, Paper, or Scissors')
human_choice = input()
def choice_to_int(num):
    if num == 'Rock':
        human_choice = 1
    elif num == 'Paper':
        human_choice = 2
    elif num == 'Scissors':
        human_choice = 3
    else:
        return
choice_to_int(human_choice)
def find_winner(choice1, choice2):
    if choice1 == 1 and choice2 == 2:
        print('Paper beats rock, computer wins')
    elif choice1 == 2 and choice2 == 3:
        print('Scissors beats paper, computer wins')
    elif choice1 == 3 and choice2 == 1:
        print('Rock beats scissors, computer wins')
    elif choice1 == 2 and choice2 == 1:
        print('Paper beats rock, player wins')
    elif choice1 == 3 and choice2 == 2:
        print('Scissors beats paper, player wins')
    elif choice1 == 1 and choice2 == 3:
        print('Rock beats scissors, player wins')
    else:
        print('Tie')
if computer_choice == 1:
    print('Computer chooses Rock')
elif computer_choice == 2:
    print('Computer Chooses Paper')
else:
    print('Computer Chooses scissors')
find_winner(computer_choice, human_choice)