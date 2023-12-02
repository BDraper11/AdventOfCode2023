from AoC2023 import *
import re

class Game:
    def __init__(self,Game):
        self.ID = int()
        self.Sets = list()
        self.NumSets = int()

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
            self.ID = ParseID(Game)
            self.Sets = ParseSets(Game)
            self.NumSets = len(self.Sets)
            return self
        thisGame = ParseGame(Game)
        return None
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
    
    reds = list()
    greens = list()
    blues = list()
    temp = [aGame for aGame in Games if not [aSet for aSet in aGame.Sets if not CheckSet(aSet,REDLIMIT,GREENLIMIT,BLUELIMIT)]]
    output = sum([x.ID for x in temp])
    print("breakpoint")
    return output

def Puzz2(Games):
    return 0

if __name__ == "__main__":
    input = GetInput(2,False)
    Execute = 1

    Games = GetGames(input)

    if (Execute & 0b01):
        Puzz1Ans = Puzz1(Games)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    elif(Execute & 0b10):
        Puzz2Ans = Puzz2(Games)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")