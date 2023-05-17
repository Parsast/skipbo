import random 

class Card:

def __init__(self,value,color):
        self.value = value
        self.color = color
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self,cards = []):
        self.cards = cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0)
    
    def is_empty(self):
        return len(self.cards) == 0

class Hand:
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

class Pile:
    
    def __init__(self, cards= []):
        self.cards = cards
    
    def add_card(card):
        self.cards.append(card)
    
    def remove_card():
        return self.cards.pop(0)

    def is_empty():
        return len(cards) == 0

    def top_card():
        return self.cards[0]

class DiscardPile(Pile):
    
    def pr():
        pass

class BuildPile(Pile):
    
