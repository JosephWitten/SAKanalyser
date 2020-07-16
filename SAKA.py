import sys
import string
import collections
import codecs

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
isHex = True
optionsArray = ["-cC", "-e"]
helpArray = ["-h", "-H", "-help", "--help"]
options = False

def printGuide():
    print("Syntax for this tool is as follows:\npython SAKA.py <options> <encryption>")

def printHelp():
    print("\n")
    print("-e: Input string. This is the encryption or string you want to analyse")
    print("-cC: Caeser Cipher. Show the results of the caeser chiper")
    print("")
    exit()

def printSummary():
    print("{}".format(colours.blue))
    print("{}General info{}".format(colours.underline, colours.reset))
    print("{}Your word is: \"{}\"".format(colours.blue, masterWord))
    print("Length: {}".format(len(masterWord)))
    print("{}".format(colours.reset))
    exit()

arguments = sys.argv
print(arguments)


def checkForOptions():
    for i in optionsArray:
        if (i in arguments):
            return True
    return False


def executeOptions():
    if ("-cC" in arguments):
        caeser()
        options = True



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
    for i in range(0, len(masterWord)):
        if (masterWord[i] not in hexChars):
            isHex = False
    return True

def doHex():
    print("-------------- Hex --------------")
    if(isHex):
        print("Your word could be hex")
        try:
            masterWordInstance = masterWord
            masterWordInstance = masterWordInstance.replace(" ", "")
            print(masterWordInstance)
            decoded = codecs.decode(masterWordInstance, "hex")
            print("It would convert into {}".format(decoded))
        except:
            print("try a different decoder")
    else:
        print("Your word is not hex")
    print("---------------------------------")


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