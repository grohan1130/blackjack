import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.isDrawn = False
    
    def get_card_suit(self):
        return self.suit
    
    def get_card_number_value(self):
        return self.value
    
    def get_card_face_value(self):
        if self.value == 1:
            return "Ace"
        elif self.value == 11: 
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13: 
            return "King"
        else: 
            return self.value
        
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    def __init__(self):
        self.cards = []
        for suit in Deck.suits: 
            for i in range (1, 14):
                self.cards.append(Card(suit, i))
    
    def shuffle(self): 
        random.shuffle(self.cards)
    
    def draw(self):
        undrawn_cards = [card for card in self.cards if not card.isDrawn]
        
        if not undrawn_cards:
            return None  # All cards have been drawn
        
        # Randomly select an undrawn card
        drawn_card = random.choice(undrawn_cards)
        drawn_card.isDrawn = True 
        return drawn_card
        

    

