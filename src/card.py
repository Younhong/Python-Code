import random
FACES = list(range(2,11)) + ['JACK','Queen','King','Ace']
SUITS = ['Clubs','Diamonds','Hearts','Spades']
class Card(object):
    def __init__(self,face,suit):
        self.face = face
        self.suit = suit
    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10    
    def __str__(self):
        article = "a "
        if self.face in [8, "Ace"]: article = "an "
        return (article + str(self.face)+" of " + self.suit)
class Deck():
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()
hand = [Card("Ace", "Spades"),Card(8, "Diamonds"),
        Card("Jack", "Hearts"),Card(10, "Clubs")]
for card in hand:
    print (card, "has value", card.value())
num_players = 3
num_cards = 5
deck = Deck()
hands = []
for j in range(num_players):
    hands.append([])
for i in range(num_cards):
    for j in range(num_players):
        card = deck.draw()
        hands[j].append(card)
        print ("Player", j+1, "draws", card)
for j in range(num_players):
    print ("Player %d's hand (value %d):" % (j+1, hand_value(hands[j])))
    for card in hands[j]:
        print (" ", card)