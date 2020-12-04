import sys
import time
import re
from utils import readFile

def organizeItem(item):
    entry = item.split(" ")
    collection = {tuple(row.split(":")) for row in entry}
    return dict(collection)
    

def extractPassport(content):
    passportInfoCollection = []
    passportEntry = ""
    for row in content:
        if row != "":
            passportEntry = passportEntry + " " + row
        else:
            passportInfoCollection.append(organizeItem(passportEntry.strip()))
            passportEntry = ""

    return passportInfoCollection

def isDigits(s):
    pattern = "\d+"
    expression = re.compile(pattern)
    if expression.fullmatch(s):
        return True
    return False

def isBetween(x, lowLim, highLim):
    return x >= lowLim and x <= highLim

def isValidHeight(height):
    value = height[0:len(height)-2]
    unit = height[len(height)-2:len(height)]
    if not isDigits(value):
        return False
    
    if unit == "cm" and isBetween(int(value), 150, 193):
        return True
    
    if unit == "in" and isBetween(int(value), 59, 76):
        return True
    
    return False

def isValidColor(color):
    pattern = "#[0-9a-f]{6}"
    expression = re.compile(pattern)
    if expression.fullmatch(color):
        return True
    return False

def isValidEye(eye):
    pattern = "(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)"
    expression = re.compile(pattern)
    if expression.fullmatch(eye):
        return True
    return False

def isValidPID(pid):
    pattern = "\d{9}"
    expression = re.compile(pattern)
    if expression.fullmatch(pid):
        return True
    return False



def checkValidationFields(item):
    if not isDigits(item["byr"]) or not isBetween(int(item["byr"]), 1920, 2003):
        return False
    if not isDigits(item["iyr"]) or not isBetween(int(item["iyr"]), 2010, 2020):
        return False
    if not isDigits(item["eyr"]) or not isBetween(int(item["eyr"]), 2020, 2030):
        return False
    if not isValidHeight(item["hgt"]):
        return False
    if not isValidColor(item["hcl"]):
        return False
    if not isValidEye(item["ecl"]):
        return False
    if not isValidPID(item["pid"]):
        return False
    return True

def containsFields(item, fields, validation=False):
    result = True
    for field in fields:
        if field not in item:
            result = False
    if validation:
        result = checkValidationFields(item)
        print(result)
    return result


def main():
    fileName = sys.argv[1]
    content = readFile(fileName)
    
    passportInfoCollection = extractPassport(content)

    FIELDS = ("hcl", "iyr", "byr", "hgt", "eyr", "ecl", "pid")
    count = 0
    validField = 0
    for passportInfo in passportInfoCollection:
        if containsFields(passportInfo, FIELDS):
            print(passportInfo)
            count = count + 1
            if containsFields(passportInfo, FIELDS, validation=True):
                validField = validField + 1

    print("Total number of passports: {0}".format(len(passportInfoCollection)))
    print("Number passports with all field: {0}".format(count))
    print("Number passports with all valid:  {0}".format(validField))

if __name__ == '__main__':
    main()
    