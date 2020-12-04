import sys
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


def checkPattern(s, regex):
    if regex.fullmatch(s):
        return True
    return False
    

def isDigits(s):
    return checkPattern(s, re.compile("\d+"))

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

def isValidHair(color):
    return checkPattern(color, re.compile("#[0-9a-f]{6}"))

def isValidEye(eye):
    return eye in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def isValidPID(pid):
    return checkPattern(pid,re.compile("\d{9}"))

def isValidBirth(birth):
    return isDigits(birth) and isBetween(int(birth), 1920, 2003)
        
def isValidIssue(issue):
    return isDigits(issue) and isBetween(int(issue), 2010, 2020)
    
def isValidExpiration(expiration):
    return isDigits(expiration) and isBetween(int(expiration), 2020, 2030)


def validateFields(item):
    return all([
        isValidBirth(item["byr"]),
        isValidExpiration(item["eyr"]),
        isValidEye(item["ecl"]),
        isValidHair(item["hcl"]),
        isValidHeight(item["hgt"]),
        isValidIssue(item["iyr"]),
        isValidPID(item["pid"])
    ])

def containsFields(item, fields):
    return all(key in item for key in fields)

def main():
    fileName = sys.argv[1]
    content = readFile(fileName)
    
    passportInfoCollection = extractPassport(content)

    FIELDS = ("hcl", "iyr", "byr", "hgt", "eyr", "ecl", "pid")
    count = 0
    validField = 0
    for passportInfo in passportInfoCollection:
        if containsFields(passportInfo, FIELDS):
            count = count + 1
            if validateFields(passportInfo):
                validField = validField + 1

    print("Total number of passports: {0}".format(len(passportInfoCollection)))
    print("Number passports with all fields present: {0}".format(count))
    print("Number passports with all fields valid:  {0}".format(validField))

if __name__ == '__main__':
    main()
    