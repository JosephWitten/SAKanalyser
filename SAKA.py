import sys
import string
import collections
import codecs

def printGuide():
    print("Syntax for this tool is as follows:\npython SAKA.py <encryption>")


arguments = sys.argv
if (len(arguments) != 2):
    printGuide()
    exit()
else:
    masterWord = arguments[1]

length = len(masterWord)
print("")
print("------- Starting ----------------")
print("Your word is \"{}\"".format(masterWord))
print("Your word is {} characters long".format(length))
print("---------------------------------")
print("")

#caeser
print("------- Caeser cipher/ ROT ------")
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
    print("| ROT {} is {} |".format(i, newWord))
print("-------------------------------")

hexChars = list(string.hexdigits)
hexChars.append(" ")
hexChars.append(",")
hexChars.append(".")
hexChars.append("x")
hexChars.append("X")
print("")
isHex = True
for i in range(0, len(masterWord)):
    if (masterWord[i] not in hexChars):
        isHex = False

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

