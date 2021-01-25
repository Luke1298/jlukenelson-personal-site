import collections


class PokerHand():
    def __init__(self, cards):
        """Expects cards to be a string of cards, seperated by a space, such as:
            5H 5C 6S 7S KD
        """
        self.specialty = ["T", "J", "Q", "K", "A"]
        def parseType(t):
            if t not in self.specialty:
                return int(t)
            else:
                return 10 + self.specialty.index(t)
        self.cards = [(parseType(c[0]), c[1]) for c in cards.split(" ")]
        self.cards = sorted(self.cards, key=lambda x: x[0])
    
    def cardsToString(self, cards):
        def parseBackType(t):
            if t>=10:
                return self.specialty[t-10]
            else:
                return str(t)
        return " ".join([parseBackType(card[0]) + card[1] for card in cards])
        
    def _straightflush(self):
        return all([self.cards[0][1] == c[1] for c in self.cards]) and all([self.cards[i][0]+1 == self.cards[i+1][0] for i in range(len(self.cards)-1)])
    
    def _fourOfAKind(self):
        counter = collections.Counter([c[0] for c in self.cards])
        if max(counter.values()) == 4:
            for key, value in counter.items():
                if value == 4: 
                    return key
        return False
    
    def _fullHouse(self):
        counter = collections.Counter([c[0] for c in self.cards])
        if len(counter) == 2 and max(counter.values()) == 3:
            for key, value in counter.items(): 
                if value == 3: 
                    return key
        return False
    
    def _flush(self):
        return all([self.cards[0][1] == c[1] for c in self.cards])
        
    def _straight(self):
        return all([self.cards[i][0]+1 == self.cards[i+1][0] for i in range(len(self.cards)-1)])
    
    def _threeOfAKind(self):
        counter = collections.Counter([c[0] for c in self.cards])
        if max(counter.values()) == 3:
            for key, value in counter.items():
                if value == 3: 
                    return key
        return False
      
    def _twopair(self):
        counter = collections.Counter([c[0] for c in self.cards])
        if max(counter.values()) == 2 and collections.Counter(counter.values())[2] == 2:
            return max(key for key, value in counter.items() if value == 2)
        return False      
        
    def _pair(self):
        counter = collections.Counter([c[0] for c in self.cards])
        if max(counter.values()) == 2:
            for key, value in counter.items():
                if value == 2: 
                    return key
        return False
    def rank(self):
        """Returns the rank of the hand, with a tuple of the value of that rank -- 
            If applicable if not, then false"""
        if self._straightflush():
            return 8, self.cards[-1][0]#Note, we don't distinguish between flush and royal, because of the second index here!
        elif self._fourOfAKind():
            return 7, self._fourOfAKind()
        elif self._fullHouse():
            return 6, self._fullHouse()
        elif self._flush():
            return 5, self.cards[-1][0]
        elif self._straight():
            return 4, self.cards[-1][0]
        elif self._threeOfAKind():
            return 3, self._threeOfAKind()
        elif self._twopair():
            return 2, self._twopair()
        elif self._pair():
            return 1, self._pair()
        else:
            return 0, self.cards[-1][0]
    def getHighCardMinusPair(self):
        relcards = [card for card in self.cards if card[0] != self._pair()]
        return relcards[-1][0]
    def getHighCardMinusTwoPair(self):
        relcards = [card for card in self.cards if card[0] != self._twopair()]
        return PokerHand(self.cardsToString(relcards))
        
    def __gt__(self, other):
        if self.rank()[0] > other.rank()[0]:
            return True
        elif self.rank()[0] == other.rank()[0]:
            if self.rank()[1] > other.rank()[1]:
                return True
            elif self.rank()[1] == other.rank()[1]:
                if self.rank()[0] == 1:
                    return self.getHighCardMinusPair() > other.getHighCardMinusPair()
                elif self.rank()[0] == 2:
                    return self.getHighCardMinusTwoPair() > other.getHighCardMinusTwoPair()
                else:
                    return "ERROR"
            else:
                return False
        else:
            return False
            
import os
import sys



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p054_poker.txt")

file = open(src_filename, "r")

src = file.read()

p1wins = 0

for line in src.split("\n"):
    if len(line) > 10:
        p1 = line[:14].strip()
        p2 = line[15:].strip()
        p1wins += (PokerHand(p1) > PokerHand(p2))
        
print p1wins