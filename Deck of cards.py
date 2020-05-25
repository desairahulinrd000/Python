import random as rd
class Card(object):
    def __init__(self,suit,val):
        self.suit=suit
        self.value=val
        
    def show(self):
        print(f"{self.value} of {self.suit}")
              
class Deck(object):
    def __init__(self):
        self.cards=[]
        self.build()
        
    def build(self):
        types=["Spades","Clubs","Diamonds","Hearts"]
        for s in types:
            for v in range(1,14):
                self.cards.append(Card(s,v))
                
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
          for i in range(len(self.cards)-1,0,-1):
                r=rd.randint(0,i)
                self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
    def drawCard(self): 
        return self.cards.pop()
    
    
class Player(object):
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()
    def discard(self):
        return self.hand.pop()
