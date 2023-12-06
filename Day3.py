from AoC2023 import *
import re

class Schematic:
    def __init__(self,input):
        self.data = input
        self.length = len(input)
        self.width = len(input[0])

class PartNum:
    def __init__(self):
        self.Value = int()
        self.StartIdx = int()
        self.EndIdx = int()

def FindPartNums(input):
    PartNums = list()
    PartNumsIdx = list()
    for line in input.data:
        PartNums.append(re.findall(r'\d+',line))
        PartNumsIdx.append([(m.start(0), m.end(0)) for m in re.finditer(r'\d+',line)])
    return PartNums, PartNumsIdx

def FindSymbols(input):
    Symbols = list()
    SymbolsIdx = list()
    for line in input.data:
        Symbols.append(re.findall(r'(?u)[^0-9\.]',line))
        SymbolsIdx.append([(m.start(0), m.end(0)) for m in re.finditer(r'[^0-9\.]',line)])
    return Symbols, SymbolsIdx

def CheckSymbolProximity(lineRange,elementRange,SymbolsIdx):
    temp = False
    for lineIdx in range(lineRange[0],lineRange[1]+1,1):
        for symbol in SymbolsIdx[lineIdx]:
            if((symbol[0] >= elementRange[0]) and (symbol[0] <= elementRange[1])):
                return True
    return temp

def ConfirmPartNumber(PartNums, PartNumsIdx, Symbols, SymbolsIdx, gridSize):
    ConfirmedPartNums = list()
    for lineIdx,line in enumerate(PartNums):
        for candidateIdx,candidate in enumerate(line):
            lineRange = (max(0,lineIdx-1),min(gridSize[1]-1,lineIdx+1))
            candidateRange = PartNumsIdx[lineIdx][candidateIdx]
            elementRange = (max(0,candidateRange[0]-1),min(gridSize[0]-1,candidateRange[1]))
            if (CheckSymbolProximity(lineRange,elementRange,SymbolsIdx)):
                ConfirmedPartNums.append(int(candidate))
    return ConfirmedPartNums

def FindGear(input):
    Gears = list()
    GearsIdx = list()
    for line in input.data:
        Gears.append(re.findall(r'[*]',line))
        GearsIdx.append([(m.start(0), m.end(0)) for m in re.finditer(r'[*]',line)])
    return Gears, GearsIdx

def CheckNGetGearRatio(lineRange,elementRange,PartNums,PartNumsIdx):
    temp = False
    proximValTable = list()
    proximTruthTable = list()
    countPNProxim = 0
    for lineIdx in range(lineRange[0],lineRange[1]+1,1):
        for idx, PartNumLoc in enumerate(PartNumsIdx[lineIdx]):
            PNVal = PartNums[lineIdx][idx]
            PNRange = [x for x in range(PartNumLoc[0],PartNumLoc[1],1)]
            searchRange = [x for x in range(elementRange[0],elementRange[1]+1,1)]
            proximValTable.append(PNVal)
            proximTruthTable.append(any([x in searchRange for x in PNRange]))

    if proximTruthTable.count(True) ==2:
        n = 1
        for i,x in enumerate(proximValTable):
            if proximTruthTable[i]:
                n = n*int(x)
        return n
    return temp

def ConfirmGear(Gears, GearsIdx, PartNums, PartNumsIdx, gridSize):
    ConfirmedGears = list()
    for lineIdx,line in enumerate(Gears):
        for candidateIdx,candidate in enumerate(line):
            lineRange = (max(0,lineIdx-1),min(gridSize[1]-1,lineIdx+1))
            candidateRange = GearsIdx[lineIdx][candidateIdx]
            elementRange = (max(0,candidateRange[0]-1),min(gridSize[0]-1,candidateRange[1]))

            check = CheckNGetGearRatio(lineRange,elementRange,PartNums,PartNumsIdx)
            if (check is not False):
                ConfirmedGears.append(check)
    return sum(ConfirmedGears)




def Puzz1(input):
    output = 0
    schematic = Schematic(input)
    PartNums, PartNumsIdx = FindPartNums(schematic)
    Symbols, SymbolsIdx = FindSymbols(schematic)
    ConfirmedPartNums = ConfirmPartNumber(PartNums, PartNumsIdx, Symbols, SymbolsIdx, (schematic.length,schematic.width))
    output = sum(ConfirmedPartNums)
    return output
def Puzz2(input):
    output = 0
    schematic = Schematic(input)
    PartNums, PartNumsIdx = FindPartNums(schematic)
    Gears, GearsIdx = FindGear(schematic)
    ConfirmedGears = ConfirmGear(Gears, GearsIdx, PartNums, PartNumsIdx, (schematic.length,schematic.width))
    output = ConfirmedGears
    return output
if __name__ == "__main__":
    input = GetInput(3,False)

    Execute = 2
    if (Execute & 0b01):
        Puzz1Ans = Puzz1(input)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    elif(Execute & 0b10):
        Puzz2Ans = Puzz2(input)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")