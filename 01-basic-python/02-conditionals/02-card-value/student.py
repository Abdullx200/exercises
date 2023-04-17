# Write your code here
def card_value(card):
    if card == "Jack":
        return 11
    elif card == "Queen":
        return 12
    elif card == "King":
        return 13
    elif card == "Ace":
        return 1
    else:
        return int(card)