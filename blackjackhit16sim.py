import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return self.rank + ' of '+ self.suit

class Deck():

    def __init__(self):

        self.deck = []
        self.no_of_decks = 0

        for i in range(0, 8):
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))
                    
                    

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The Deck has: ' + deck_comp
        

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card



class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

    



win = 0
draw = 0
loss = 0

for j in range(0, 100):
    test_deck = Deck()
    test_deck.shuffle()
    test_player = Hand()

    if test_player.value >= 17:
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Hand()
    else:
        test_player.add_card(test_deck.deal())
        test_player.add_card(test_deck.deal())
        test_player.adjust_for_ace()


    dealer_hand = Hand()
    dealer_hand.add_card(test_deck.deal())
    dealer_hand.add_card(test_deck.deal())
    dealer_hand.adjust_for_ace()

    while dealer_hand.value < 17:
        hit(test_deck, dealer_hand)

    

    if dealer_hand.value > 21:
        win += 1

    if dealer_hand.value > 16 and dealer_hand.value <= 21:
        loss += 1

    

'''for card in dealer_hand.cards:
    print(card)'''
print('wins = ' + str(win) +' losses = '+ str(loss))

