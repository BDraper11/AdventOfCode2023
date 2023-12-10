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
    fileNames = [baseName+".py",baseName+"Input.txt",baseName+"InputTest.txt"]
    with open("start.txt") as file: start = file.read()
    fileContent = [start,"",""]

    for i,file in enumerate(fileNames):
        with open(file, 'a') as file:
            file.write(fileContent[i])

"""

"""