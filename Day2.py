from AoC2023 import *
import re

class Game:
    def __init__(self,Game):
        self._ID = int()
        self._Sets = list()
        self._NumSets = int()
        self._Power = int()

        def ParseGame(Game):
            def ParseID(Game):
                ID = int(Game.split(":")[0].split()[-1])
                return ID
            def ParseSets(Game):
                def ParseSet(Set):
                    retSet = dict()
                    tempSet = [x.strip() for x in Set.split(",")]
                    tempSet2 = [x.split() for x in tempSet]
                    [retSet.update({x[-1]:x[0]}) for x in tempSet2]
                    return retSet
                
                Sets = list()
                tempSets = Game.split(":")[-1].split(";")
                for Set in tempSets:
                    Sets.append(ParseSet(Set))
                return Sets
            self._ID = ParseID(Game)
            self._Sets = ParseSets(Game)
            self._NumSets = len(self._Sets)
            return self
        
        thisGame = ParseGame(Game)
        return None
    
    @property
    def Sets(self): return self._Sets
    @Sets.setter
    def Sets(self, value): self._Sets = value
    @Sets.deleter
    def Sets(self): del self._Sets

    @property
    def ID(self): return self._ID
    @ID.setter
    def ID(self, value): self._ID = value
    @ID.deleter
    def ID(self): del self._ID
    
    @property
    def Power(self): return self._Power
    @Power.setter
    def Power(self, value): self._Power = value
    @Power.deleter
    def Power(self): del self._Power

    def CalcPower(self):
        maxReds = int()
        maxGreens = int()
        maxBlues = int()

        for Set in self.Sets:
            if "red" in Set:
                maxReds = max(maxReds,int(Set["red"]))
            if "green" in Set:
                maxGreens = max(maxGreens,int(Set["green"]))
            if "blue" in Set:
                maxBlues = max(maxBlues,int(Set["blue"]))
        self._Power = (maxReds*maxGreens*maxBlues)
        return self._Power
def GetGames(input):
    Games = list()
    for line in input:
        thisGame = Game(line)
        Games.append(thisGame)
    return Games
def CheckSet(Set,REDLIMIT,GREENLIMIT,BLUELIMIT):
    if "red" in Set:
        c1 = int(Set["red"])<=REDLIMIT
    else:
        c1 = True
    if "green" in Set:
        c2 = int(Set["green"])<=GREENLIMIT
    else:
        c2 = True
    if "blue" in Set:
        c3 = int(Set["blue"])<=BLUELIMIT
    else:
        c3 = True
    return (c1 and c2 and c3)
def Puzz1(Games):
    REDLIMIT = 12
    GREENLIMIT = 13
    BLUELIMIT = 14
    
    temp = [aGame for aGame in Games if not [aSet for aSet in aGame.Sets if not CheckSet(aSet,REDLIMIT,GREENLIMIT,BLUELIMIT)]]
    output = sum([x.ID for x in temp])
    print("breakpoint")
    return output
def Puzz2(Games):
    output = [Game.CalcPower() for Game in Games]
    output = sum(output)
    return output
if __name__ == "__main__":
    input = GetInput(2,False)
    Games = GetGames(input)

    Execute = 2
    if (Execute & 0b01):
        Puzz1Ans = Puzz1(Games)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    elif(Execute & 0b10):
        Puzz2Ans = Puzz2(Games)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")