#! /usr/local/bin/python3.4
import sys
import re
import glob

def isNameValid(signalName):
    worder = re.search(r"^([a-z]{3}\-[0-9]{3}$)", signalName, re.X | re.I)
    if worder:
        return True
    else:
        return False


def loadSignal(signalName, signalFolder):
    floatnum = []
    c = 0
    if not isNameValid(signalName):
        raise ValueError(signalName + " is not valid")
    totaloc = signalFolder + "/" + signalName + ".txt"
    try:
        open(totaloc, "r")
    except:
        raise OSError(signalName + " is missing from folder")
    with open(totaloc, "r") as signalFile:
        lines = signalFile.readlines()
    for line in lines:
        line = line.strip()

        try:
            val = float(line)
        except:
            c = c + 1
        else:
            floatnum.append(float(line))
    ans = (floatnum, c)
    return ans


def isSignalAcceptable(signal, valueRange, maxCount):
    min, max = valueRange
    min = float(min)
    max = float(max) iu
    counter = 0
    test = 0
    num = 0
    if len(signal) == 0:
        raise ValueError("Signal contains no data")

    for line in signal:
        if line > max or line < min:
            counter = counter + 1
    if counter > maxCount:
        return False
    else:
        return True


