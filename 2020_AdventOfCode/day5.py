from utils import readFile
import sys
import math

def main():
    fileName = sys.argv[1]
    boardingPasses = readFile(fileName)

    # print(boardingPasses)
    takenSeats = []
    for boarding in boardingPasses:
        seat = {}
        highLim = 127
        lowLim = 0
        row = -1  
        for direction in boarding[0:6]:
            if direction == "F":
                highLim = highLim - int((highLim-lowLim+1)/ 2)
            elif direction == "B":
                lowLim = lowLim + int((highLim-lowLim+1)/ 2)
        if boarding[6] == "F":
            row = lowLim
        elif boarding[6] == "B":
            row = highLim
        
        lowLim = 0
        highLim = 7
        col = -1
        for direction in boarding[6:]:
            if direction == "L":
                highLim = highLim - int((highLim-lowLim+1)/ 2)
            elif direction == "R":
                lowLim = lowLim + int((highLim-lowLim+1)/ 2)
        if boarding[9] == "L":
            col = lowLim
        elif boarding[9] == "R":
            col = highLim
        
        takenSeats.append(dict([("row",row),("col",col),("id",row*8+col)]))
    
    ID = [ seat["id"] for seat in takenSeats]
    print(max(ID))

    ID.sort()
    
    for i in range(1, len(ID)-1): 
        if ID[i] - ID[i-1] > 1:
            print(ID[i])
        elif ID[i+1] - ID[i] > 1:
            print(ID[i])
        
        
if __name__ == '__main__':
    main()
    
