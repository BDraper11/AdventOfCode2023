from AoC2023 import *
import numpy as np

def GetInput(d,Test = False):
    if Test:
        cmdStr = "Day"+str(d)+"InputTest.txt"
    else:
        cmdStr = "Day"+str(d)+"Input.txt"
    
    with open(cmdStr) as f:
        input = f.read()
    return input

def GetSeeds(allData,Puzz = 1):
    seeds = allData[0].split(":")[1].strip().split()
    seeds = [int(x) for x in seeds]
    if(Puzz == 1): pass
    elif(Puzz == 2):
        i = 0
        newSeeds = list()
        while (i < (len(seeds)-1)):
            newSeeds.append([x for x in range(seeds[i],(seeds[i]+seeds[i+1]))])
            i +=2
        x = set()
        for y in newSeeds:
            x = x.union(set(y))
        seeds = x
    else: return 0
    return seeds

def GetMaps(allData):
    mapsRaw = allData[1:]
    mapNames = [x.split(":")[0] for x in mapsRaw]
    mapData = [x.split(":")[1] for x in mapsRaw]
    mapData = [x.strip().splitlines() for x in mapData]
    
    maps = list()
    for map in mapData:
        thisMap = list()
        for segment in map:
            x = [int(x) for x in segment.split()]
            thisMap.append(x)
        thisMap = np.array(thisMap)
        #print(thisMap), print("\n")
        thisMap = thisMap[thisMap[:, 1].argsort()]
        #print(thisMap), print("\n")
        maps.append(thisMap)
    return maps, mapNames

def Puzz1(input):
    output = 0
    allData = input.split("\n\n")
    seeds = GetSeeds(allData)
    maps, mapNames = GetMaps(allData)

    seedRoutes = list()
    for seed in seeds:
        seedRoute = list()
        lookup = seed
        print("\nWriting starteing seed: " + str(lookup))
        seedRoute.append(lookup)
        for j,map in enumerate(maps):
            print(mapNames[j])
            #print(map)
            dest = [x[0] for x in map]
            source = [x[1] for x in map]
            length = [x[2] for x in map]
            c1 = (lookup < source[0])
            mapSourceEnd = (source[-1]+length[-1])
            c2 = (lookup > (source[-1]+length[-1]))#, print(lookup,mapSourceEnd,source[-1],length[-1])
            c3 = (lookup > mapSourceEnd)
            if (c1 or c3):
                print(str(lookup) + " is not within; " + str(source[0]) + " or " + str(mapSourceEnd))
                seedRoute.append(lookup)
            else:
                for i,segmentSourceStart in enumerate(source):
                    segmentSourceEnd = segmentSourceStart + length[i]
                    if (lookup >= source[i] and lookup < (source[i]+length[i])): ##### Potential issue here but lets see.
                        destOutput = int(dest[i]+(lookup-source[i]))
                        print(str(lookup) + " maps to: " + str(destOutput) + ". Writing " + str(destOutput))
                        lookup = destOutput
                        seedRoute.append(lookup)
                        break
        seedRoutes.append(seedRoute)
        print(seedRoute)
    print("\n")
    print(seedRoutes)
    output = min([x[-1] for x in seedRoutes])
    return output

def Puzz2(input,Puzz = 2):
    output = 0
    allData = input.split("\n\n")
    seeds = GetSeeds(allData,2)
    maps, mapNames = GetMaps(allData)


    return output

if __name__ == "__main__":
    input = GetInput(5,False)

    Execute = 1
    if (Execute & 0b01):
        Puzz1Ans = Puzz1(input)
        print(Puzz1Ans), pyperclip.copy(Puzz1Ans)
    if(Execute & 0b10):
        Puzz2Ans = Puzz2(input)
        print(Puzz2Ans), pyperclip.copy(Puzz2Ans)

    print("Done")