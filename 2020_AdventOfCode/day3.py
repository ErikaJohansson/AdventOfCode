import sys
from utils import readFile


def updatePosition(posDown, posRight, mapWidth, slopeDown, slopeRight):
    
    return [posDown + slopeDown, (posRight + slopeRight) % mapWidth]


def countTrees(map, slope):
    posDown, posRight = 0,0
    mapWidth = len(map[0])
    treeCount = 0
    while posDown < len(map):
        if map[posDown][posRight] == "#":
            treeCount = treeCount + 1
        [posDown, posRight] = updatePosition(posDown, posRight, mapWidth, slope["D"], slope["R"])
    return treeCount


def main():
    inputFile = sys.argv[1]
    map = readFile(inputFile)
    print("Input File: {0}".format(inputFile))
    
    encounteredTrees = []
    slopeAlternatives = [{"D":1, "R":1}, {"D":1, "R":3}, {"D":1,"R":5}, {"D":1, "R":7}, {"D":2, "R":1}]

    for i in range(len(slopeAlternatives)):
        treeCount = countTrees(map, slopeAlternatives[i])
        print("For slope R{1} D{0} number of encountered trees are: {2}".format(slopeAlternatives[i]["D"], slopeAlternatives[i]["R"], treeCount))
        encounteredTrees.append(treeCount)
        
    treeProduct = 1
    for trees in encounteredTrees:
        treeProduct = treeProduct * trees
    
    print("Encountered trees multiplied together: {0}".format(treeProduct))
        
if __name__ == "__main__":
    main()