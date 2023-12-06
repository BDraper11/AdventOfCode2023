from AoC2023 import *
import re
from collections import defaultdict

class Scratchcard:
    def GetWinners(self):
        self._Winners = [self._CardNums[i] for i,y in enumerate([x in self._WinNums for x in self._CardNums]) if y]
    def GetScore(self):
        if len(self._Winners) == 0:
            self._Score = 0
        elif len(self._Winners) == 1:
            self._Score = 1
        else:
            self._Score = 2**(len(self._Winners)-1)
    def GetWonCardIDs(self):
        self._WonCardIDs = [x + self._ID for x in range(1,len(self._Winners)+1)]
    def IncrementCardCount(self):
        self._CardCount +=1
    def AddWonCard(self, newCard):
        self._WonCards.append(newCard)
    def __init__(self,Id,WinNums,CardNums):
        self._ID = Id
        self._WinNums = WinNums
        self._CardNums = CardNums
        self._Winners = None
        self._Score = None
        self._WonCardIDs = None
        self._CardCount = 0
        self._WonCards = list()

        self.GetWinners()
        self.GetScore()
        self.GetWonCardIDs()
        self.IncrementCardCount()

        @property
        def WonCards(self): return self._WonCards
        @WonCards.setter
        def WonCards(self,data): Scratchcard(data)
        @WonCards.deleter
        def WonCards(self): del self._WonCards

        return None
 
def ParseCard(card):
    def GetCardID(inputLine):
        return int(re.findall(r'\d+',inputLine)[0])
    
    def GetWinNums(inputLine):
        inputLine = inputLine.split(":")[1].strip()
        inputLine = inputLine.split("|")[0].split()
        return [int(x) for x in inputLine]
    
    def GetCardNums(inputLine):
        inputLine = inputLine.split("|")[1].split()
        return [int(x) for x in inputLine]

    Id = GetCardID(card)
    WinNums = GetWinNums(card)
    CardNums = GetCardNums(card)

    thisSC = Scratchcard(Id,WinNums,CardNums)
    return thisSC

def Puzz1(input):
    output = 0
    Scratchcards = [ParseCard(card) for card in input]

    output = sum([x._Score for x in Scratchcards])
    return output, Scratchcards

def Puzz2(Scratchcards):
    AllCards = defaultdict(int)
    for i,Card in enumerate(Scratchcards):
        AllCards[i+1] +=1
        for WonCard in Card._WonCardIDs:
            AllCards[WonCard] += AllCards[i+1]
    output = sum(AllCards.values())
    return output

if __name__ == "__main__":
    input = GetInput(4,False)

    Execute = 3
    if (Execute & 0b01):
        Puzz1Ans, Scratchcards = Puzz1(input)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    if(Execute & 0b10):
        Puzz2Ans = Puzz2(Scratchcards)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")