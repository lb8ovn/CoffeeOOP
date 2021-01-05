import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose"
    elif user_score == 0:
        return "Blackjack"
    elif user_score > 21:
        return "Bust"
    elif computer_score > 21:
        return "Computer Bust"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(user_cards)
print(computer_cards[0])
is_game_over = False
while not is_game_over:
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input('Type y to get another card, or n to stay')
        if user_should_deal == "y":
            user_cards.append(deal_card())
            print(user_cards)
        else:
            is_game_over = True

while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

compare(user_score, computer_score)