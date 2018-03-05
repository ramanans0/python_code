#! /usr/local/bin/python3.4
import sys
import re
import glob
import moduleTasks
from moduleTasks import *

def loadSignals(signalNames, signalFolder, maxNonfloatCount):
    ansdict = {}
    for signal in signalNames:
        val = []
        c = 0
        try:
            val, c = loadSignal(signal, signalFolder)
        except:
            value = None
        else:
            value = val
            if c > maxNonfloatCount:
                value = []
        ansdict[signal] = value
    return ansdict




def saveSignals(signalsDictionary, valueRange, maxCount, targetFolder):
    signals = signalsDictionary.keys()
    values = signalsDictionary.values()

    for signal, signalVal in signalsDictionary.items():
        if signalVal is not None:
            try:
                if isSignalAcceptable(signalsDictionary[signal], valueRange, maxCount):
                    totaloc = targetFolder + "/" + signal + ".txt"
                    with open(totaloc, "w") as signalFile:
                        for i in signalsDictionary[signal]:
                            signalFile.write("{0:.3f}\n".format(i))
            except:
                pass

#if __name__ == "__main__":
#    test = ["AFW-481", "HPQ-298", "NIK-876", "PXF-961", "VKY-370"]
#    dict = loadSignals(test, "Signals", 20)
#    print(dict)
#    saveSignals(dict, (-11.7, 12.0), 2, "test")
