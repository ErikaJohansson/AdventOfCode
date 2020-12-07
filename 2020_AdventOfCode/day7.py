from utils import readFile
import sys
import re

BAG_TYPE = "shiny gold"

def findNbBagsInside(color, bagRules):
    total = 0
    print("Color = '{0}'".format(color))
    for rule in bagRules:
        [outerBag, bagsInside] = re.split(" bags contain", rule, maxsplit=1)
        if color == outerBag:
            bagsInsideSeparated = re.findall("[0-9]+ [a-z]+ [a-z]+", bagsInside)
            for bags in bagsInsideSeparated:
                [nb, bagColor] = re.split(" ", bags, maxsplit=1)
                total += int(nb) + int(nb) * findNbBagsInside(bagColor, bagRules)
    return total   
 
def main():
    fileName = sys.argv[1]
    bagRules = readFile(fileName=fileName)
    
    allowedBags = {BAG_TYPE}

    startLen = 0
    endLen = 1
    lookupTimes = 0
    while endLen > startLen:
        lookupTimes += 1
        startLen = len(allowedBags)
        newAllowedBags = set()
        for rule in bagRules:
            for bagType in allowedBags:
                outerBag = re.split(" bags contain", rule, maxsplit=1)[0]
                if bagType in rule:
                    newAllowedBags.add(outerBag)
        allowedBags = allowedBags | newAllowedBags
        endLen = len(allowedBags)
    
    print("Can contain shiny gold: {0}".format(len(allowedBags)-1))
    print("LookupTimes: {0}".format(lookupTimes))
    
    total = findNbBagsInside(BAG_TYPE, bagRules)
    print("Total bags inside a shiny gold bag: ", total)
    
    
if __name__ == '__main__':
    main()
    