import sys
from utils import readFile

NB_QUESTIONS = 26


def main():
    fileName = sys.argv[1]
    form_answers = readFile(fileName)

    yesAnswers = [0] * NB_QUESTIONS
    groupQuestions = 0
    groupSize = 0
    for person in form_answers:
        if person == "":
            groupQuestions += yesAnswers.count(1) 
            yesAnswers = [0] * NB_QUESTIONS
            groupSize = 0
        else:
            groupSize += 1     
            for yes in person:
                yesAnswers[ord(yes) - ord("a")] = 1
        
    print("Questions in that at least one member per group answered yes: ", groupQuestions)

    yesAnswers = [0] * NB_QUESTIONS
    groupQuestions = 0
    groupSize = 0
    for person in form_answers:
        if person == "":
            groupQuestions += yesAnswers.count(groupSize) 
            yesAnswers = [0] * NB_QUESTIONS
            groupSize = 0
        else:
            groupSize += 1
            for yes in person:
                yesAnswers[ord(yes) - ord("a")] += 1
    
    print("Questions in that all members in a group answered yes to: ", groupQuestions)
    
    
if __name__ == '__main__':
    main()
    