from utils import readFile
import sys

def checkForSum(nb, code):
    collection = code.copy()
    collection.sort()
    lowLim = 0
    highLim = len(collection)-1
    while highLim > lowLim:
        high = collection[highLim]
        low = collection[lowLim]
        twoSum = high + low
        # print("{0} = {1} + {2}".format(twoSum, high, low))
        if twoSum == nb:
            return [True, high, low]
        elif twoSum < nb:
            lowLim += 1
        elif twoSum > nb:
            highLim -= 1
    
    return [False, -1, -1] 
    

def main():
    fileName = sys.argv[1]
    content = readFile(fileName)
    xmasCode = [int(x) for x in content]
    
    if "example" in fileName:
        preLen = 5
    else:
        preLen = 25
    wrongNb = []
    for row in range(preLen, len(xmasCode)):
        [isValid, high, low] = checkForSum(xmasCode[row], xmasCode[row-preLen:row])        
        if not isValid:
            wrongNb.append(xmasCode[row])
    
    print(wrongNb)

    invalidNb = wrongNb[0]
    lowLim = 0
    highLim = 1
    while lowLim < len(xmasCode) and highLim <= len(xmasCode):
        # print(xmasCode[lowLim:highLim])
        currentSum = sum(xmasCode[lowLim:highLim])
        if invalidNb == currentSum:
            print("Set: ", xmasCode[lowLim:highLim])
            minValue = min(xmasCode[lowLim:highLim])
            maxValue = max(xmasCode[lowLim:highLim])
            print("{0} + {1} = {2}".format(minValue, maxValue, minValue + maxValue))
            break
        elif invalidNb > currentSum:
            highLim += 1
        elif invalidNb < currentSum:
            lowLim += 1
            highLim = lowLim + 1 




if __name__ == '__main__':
    main()
    