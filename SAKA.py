import sys
import string
import collections
import codecs

#TO DO LIST/ OPTIONS:
# Input - tick
# caeser - tick
# hex -  tick


class colours:
    red = "\u001b[31m" #not this
    green = "\u001b[32m" #this
    yellow = "\u001b[33m" #could be this
    blue = "\u001b[34m" #general
    reset = "\u001b[0m" #reset
    underline = "\u001b[4m"

#GlobalVariables
hexChars = list(string.hexdigits)
hexChars.append(" ")
hexChars.append(",")
hexChars.append(".")
hexChars.append("x")
hexChars.append("X")
optionsArray = ["-cC", "-e", "-x"]
helpArray = ["-h", "-H", "-help", "--help"]
greenArray = []
yellowArray = []
redArray = []
options = False
hexResult = ""

def printGuide():
    print("Syntax for this tool is as follows:\npython SAKA.py <options> <encryption>")

def printHelp():
    print("\n")
    print("-e: Input string. This is the encryption or string you want to analyse")
    print("-cC: Caeser Cipher. Show the results of the caeser chiper")
    print("-x: Hex. Show the results of a hex decrypt")
    print("")
    exit()

def printSummary():

    #checkHex, append it the correct colour array
    isHex = checkHex()
    print(isHex)
    if (isHex):
        hexResult = doHex()
        if (hexResult == False):
            yellowArray.append("Hex")
        else:
            greenArray.append("Hex")
    else:
        redArray.append("Hex")
    
    #add caeser to yellow
    yellowArray.append("Caeser")

    print(colours.blue)
    print("{}General info{}".format(colours.underline, colours.reset))
    print("{}Your word is: \"{}\"".format(colours.blue, masterWord))
    print("Length: {}".format(len(masterWord)))
    print(colours.reset)

    #PRINT LIKELY ONES
    print(colours.green)
    for i in greenArray:
        print("[+] " + i)
    print(colours.reset)

    #PRINT MAYBE ONES
    print(colours.yellow)
    for i in yellowArray:
        print("[-] " + i)
    print(colours.reset)

    #PRINT NOT ONES
    print(colours.red)
    for i in redArray:
        print("[x] " + i)
    print(colours.reset)

    exit()

arguments = sys.argv
print(arguments)


def checkForOptions():
    temp = False
    for i in optionsArray:
        if (i in arguments):
            temp = True
    return temp


def executeOptions():
    if ("-cC" in arguments):
        caeser()
        

    if ("-x" in arguments):
        result = doHex()
        if (result == False):
            print("Try a different decoder")
        else:
            print("{}{}{}{}".format(colours.underline, colours.green, "Hex decoded", colours.reset))
            print(result)


    #caeser
def caeser():
    print("")
    print("{}{}Caeser cipher/ROT{}".format(colours.green, colours.underline, colours.reset))
    for i in range(0, 27):
        #declare var
        masterWordInstance = masterWord.lower()
        indexArray = []
        alphabet = list(string.ascii_lowercase)
        d = collections.deque(alphabet)
        newWord = ""
        #record indexes
        for j in range(0, len(masterWord)):
            if (masterWordInstance[j] in alphabet):
                indexArray.append(alphabet.index(masterWordInstance[j]))
            else:
                indexArray.append(masterWordInstance[j])
        #rotate alphabet arrays
        d.rotate(i)
        #assemble new words
        for j in range(0, len(masterWord)):
            if(masterWordInstance[j] in alphabet):
                newWord = newWord + d[indexArray[j]]
            else:
                newWord = newWord + indexArray[j]
        #print
        print("ROT {} is {} ".format(i, newWord))
    print("")
def checkHex():
    temp = True
    for i in range(0, len(masterWord)):
        if (masterWord[i] not in hexChars):
            temp = False
    return temp
def doHex():
        try:
            masterWordInstance = masterWord
            masterWordInstance = masterWordInstance.replace(" ", "")
            decoded = codecs.decode(masterWordInstance, "hex")
            return decoded
        except:
            return False

#shows guide if run alone
if (len(arguments) < 2):
    printGuide()
    exit()
#sets masterword
else:
    masterWord = arguments[len(arguments) - 1]
    if ("-e" in arguments):
        indexOfe = arguments.index("-e")
        masterWord = arguments[indexOfe + 1]
#if the second arg is -h show help
if(arguments[1] in helpArray):
    printHelp()
#if help not been called. do default summary
else:
    options = checkForOptions()

if (options == False):
    printSummary()
else:
    executeOptions()