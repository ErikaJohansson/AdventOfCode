
import re

def exactlyOne(first,  second):
    return first != second


keys = ["first", "second", "char", "password"]

passwordFile = open("corrupted_passwords.txt", "r")
corruptedPasswords = [ dict(zip(keys, re.split("-| |: ", line))) for line in passwordFile.read().split("\n")]
passwordFile.close()


nbVaildIntervalPassword = 0
for entry in corruptedPasswords:
    limCount = entry["password"].count(entry["char"])
    if limCount >= int(entry["first"]) and limCount <= int(entry["second"]):
        nbVaildIntervalPassword = nbVaildIntervalPassword + 1
              
print(f"First policy gives {nbVaildIntervalPassword} valid passwords")


nbVaildPositionPassword = 0
for entry in corruptedPasswords:
    if len(entry["password"]) >= int(entry["first"]) and len(entry["password"]) >= int(entry["second"]):
        foundInFirstPos = entry["password"][int(entry["first"])-1] == entry["char"]
        foundInSecondPos = entry["password"][int(entry["second"])-1] == entry["char"]
        if exactlyOne(foundInFirstPos,foundInSecondPos):
            nbVaildPositionPassword = nbVaildPositionPassword + 1
            
print(f"Second policy gives {nbVaildPositionPassword} valid passwords")
