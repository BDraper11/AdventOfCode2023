import logging, sys, os
import pyperclip

def GetInput(d,Test = False):
    if Test:
        cmdStr = "Day"+str(d)+"InputTest.txt"
    else:
        cmdStr = "Day"+str(d)+"Input.txt"
    
    with open(cmdStr) as f:
        input = f.read().splitlines()
    return input

def PrintOrdtoChr(start=0,end=127):
    l = range(start,end)
    for i in l:
        print("Ord ",i,"is: ",chr(i))
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug('A debug message!')
    logging.info('We processed %d records', len([1,2,3,4]))

    path = os.getcwd()
    if not os.path.exists(path):
        os.makedirs(path)

    DayNum = input("Enter Day Number: ")
    baseName = "Day"+str(DayNum)
    filenames = [baseName+".py",baseName+"Input.txt",baseName+"InputTest.txt"]

    for file in filenames:
        open(file, 'a').close()

"""
from AoC2023 import *

def Puzz1(input):
    output = 0
    return output

def Puzz2(input):
    output = 0
    return output

if __name__ == "__main__":
    input = GetInput(4,True)

    Execute = 1
    if (Execute & 0b01):
        Puzz1Ans = Puzz1(input)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    elif(Execute & 0b10):
        Puzz2Ans = Puzz2(input)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")
"""