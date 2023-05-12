import random 

Class Card:
    def __init__(self,value,color):
        self.value = value
        self.color = color
    def __str__(self):
        return f"{self.value} of {self.suit}"

Class deck:
    def __init__(self,cards):
        self.cards = cards
    
    def shuffle(self):
        return(random.shuffle(self.cards))
    def draw(self):
        return(self.cards[0])
    def is_empty(self):
        if self.cards:
            return False
        return True