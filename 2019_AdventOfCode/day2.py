import os, sys

ADD = 1
MULTIPLY = 2
STOP = 99

    
def execute(memory):
    for optCodePos in range(0,len(memory),4):
        optCode = memory[optCodePos]
        if optCode == STOP:
            return    
        firstPos = memory[optCodePos+1]
        secondPos = memory[optCodePos+2]
        resultPos = memory[optCodePos+3]
        if optCode == ADD:
            memory[resultPos] = memory[firstPos] + memory[secondPos]
        elif optCode == MULTIPLY:
            memory[resultPos] = memory[firstPos] * memory[secondPos]    



def executeProgram(program, noun, verb):
    memory = program[:]
    memory[1] = noun
    memory[2] = verb
    execute(memory)
    return memory[0]
    


def findInput(program, expectedResult):    
    for noun in range(100):
        for verb in range(100):
            result = executeProgram(program, noun, verb)
            if result == expectedResult:
                return {"noun": noun, "verb": verb}
    


fileName = sys.argv[1]
gravityAssistFile = open(fileName, "r")
gravityAssistProgram = [int(x) for x in gravityAssistFile.read().split(",")]
gravityAssistFile.close()

result = executeProgram(gravityAssistProgram, 12, 2)
print(f"Part 1: The result for the 1202 program alarm is {result}")

result = findInput(gravityAssistProgram, 19690720)
print(f"Part 2: 100 * noun + verb = 100 * {result['noun']} + {result['verb']} = {100*result['noun']+result['verb']}")