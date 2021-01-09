import random

tries = 0
answer = input(str(("Hard mode y/n")))
if answer.upper() == 'Y':
    tries = tries + 5
number = random.randint(1, 101)
def guesser():
    global tries
    while tries < 10:
        guess = input('Make a guess')
        guess = int(guess)
        if guess == number:
            print('You got it')
            return
        elif guess < number:
            print('Too Low')
        else:
            print('Too High')
        tries = tries + 1
guesser()