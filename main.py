import os, random
import time, sys
os.system('clear')
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
END = '\033[0m'
def swapPositions(list, pos1, pos2):
    """this swaps the elements of the list"""
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


#types of speed


def spslo(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") or (i != ":") or (i != ".")):
            time.sleep(0.1)
        else:
            time.sleep(0.6)


def spmod(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") or (i != ":") or (i != ".")):
            time.sleep(0.06)
        else:
            time.sleep(0.6)


def spfas(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") or (i != ":") or (i != ".")):
            time.sleep(0.03)
        else:
            time.sleep(0.02)


spfas(green + "Please choose one from the following text speeds:\n")
#speed manager

time.sleep(1)
spslo(bwhite + "a)This is slow.\n")
time.sleep(0.07)
spmod("b)This is moderate.\n")
time.sleep(0.04)
spfas("c)This is fast.\n")
time.sleep(0.02)
print(green + "Enter the letter [a/b/c]")
spc = input(":")
spc = spc.lower()
if spc == "a":
    time.sleep(0.07)
    os.system("clear")
    sp = spslo
    sp("Thank you!!\n")
elif spc == "b":
    time.sleep(0.04)
    os.system("clear")
    sp = spmod
    sp("Thank you!!\n")
elif spc == "c":
    time.sleep(0.02)
    os.system("clear")
    sp = spfas
    spslo("Thank you!!\n")
time.sleep(1)
os.system("clear")
