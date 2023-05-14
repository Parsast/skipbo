import random 

Class Card:

def __init__(self,value,color):
        self.value = value
        self.color = color
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

Class Deck:
    def __init__(self,cards = []):
        self.cards = cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0)
    
    def is_empty(self):
        return len(self.cards) == 0

Class Hand:
    def __init__(self):
        self.cards = cards

    def add_cards(card):
        self.cards.append(card)

    def remove_card(index):
        return self.cards.pop(index)

    def play_card(index):
        card = self.cards[index]
        self.remove_card(index)
        return card
