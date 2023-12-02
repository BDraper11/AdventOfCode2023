from AoC2023 import *
import re

def GetAlphaNums(line, NumDict,NumNames,NumDictAlt):
    temp = [re.search(i,line) for i in NumDictAlt]
    while any([e is not None for e in temp]):
        temp2 = [e.span()[0] if e is not None else 65535 for e in temp] #print(e.pos)
        line = line.replace(NumNames[temp2.index(min(temp2))],str(NumDictAlt[NumNames[temp2.index(min(temp2))]]))
        temp = [re.search(i,line) for i in NumDict]
    
    """temp = [re.search(i,line) for i in NumDictAlt]
    temp2 = [e.span()[0] if e is not None else 65535 for e in temp]
    line = line.replace(NumNames[temp2.index(min(temp2))],str(NumDictAlt[NumNames[temp2.index(min(temp2))]]))

    temp = [re.search(i,line) for i in NumDict]
    temp2 = [e.span()[0] if e is not None else 0 for e in temp]
    line = line.replace(NumNames[temp2.index(max(temp2))],str(NumDictAlt[NumNames[temp2.index(max(temp2))]]))
"""
    ret = line
    return ret

def GetValue(line):
    numCharArray = re.findall(r'\d+',line)
    ret = int(numCharArray[0][0] + numCharArray[-1][-1])
    return int(ret)

def Puzz1(input):
    ret = sum([GetValue(line) for line in input])
    return ret

def Puzz2(input):
    NumNames = ["one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"]
    NumConversion = ["on1e",
        "tw2o",
        "thre3e",
        "fou4r",
        "fiv5e",
        "si6x",
        "seve7n",
        "eigh8t",
        "nin9e"]
    NumDict = dict(zip(NumNames,range(1,10,1)))
    NumDictAlt = dict(zip(NumNames,NumConversion))
    temp = [GetValue(GetAlphaNums(line,NumDict,NumNames,NumDictAlt)) for line in input]
    print(sum(temp))
    ret = sum([GetValue(GetAlphaNums(line,NumDict,NumNames,NumDictAlt)) for line in input])
    return ret

if __name__ == "__main__":
    input = GetInput(1,False)
    Execute = 2

    if (Execute & 0b01):
        Puzz1Ans = Puzz1(input)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    elif(Execute & 0b10):
        Puzz2Ans = Puzz2(input)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")