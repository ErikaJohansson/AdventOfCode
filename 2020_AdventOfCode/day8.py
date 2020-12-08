from utils import readFile
import sys
import copy

def executeCode(code):
    error = 0
    instructionsExecuted = [0] * len(code)
    acculmulator = 0
    row = 0
    while row < len(code) and instructionsExecuted[row] == 0:
        instruction = code[row][0:3]
        value = int(code[row][3:])
        instructionsExecuted[row] = 1
        if instruction == "nop":
            row += 1
        elif instruction == "acc":
            acculmulator += value
            row += 1
        elif instruction == "jmp":
            row += value
    
    if row != len(code):
        error = 1
        
    return {"value": acculmulator, "error": error}

def main():
    fileName = sys.argv[1]
    bootCode = readFile(fileName=fileName)

    # Part 1
    result = executeCode(bootCode)                   
    print("The accumulated value: {0}, Error: {1}".format(result["value"], result["error"]))

    # Part 2
    for row in range(1,len(bootCode)):
        newCode = copy.deepcopy(bootCode)
        if newCode[row][0:3] != "acc":
            if newCode[row][0:3] == "jmp":
                newCode[row] = newCode[row].replace("jmp", "nop")
                result = executeCode(newCode)
            elif newCode[row][0:3] == "nop":
                newCode[row] = newCode[row].replace("nop", "jmp")
                result = executeCode(newCode)
            if result["error"] == 0:
                break
    print("The accumulated value: {0}, Error: {1}".format(result["value"], result["error"]))

if __name__ == '__main__':
    main()
    