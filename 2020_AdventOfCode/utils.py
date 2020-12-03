
def readFile(fileName):
    """Reads the entire file and returns the content in a list with each
    line a as entry stripped of trailing newlines"""

    file = open(fileName, "r")
    content = file.read().split("\n")
    file.close()
    return content