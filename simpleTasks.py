#! /usr/local/bin/python3.4
import sys

def loadFile():

    with open("signals.txt", "r") as signalFile:
        lines = signalFile.readlines()

    return lines

def getAverageBySignal(signalName):
    line = loadFile()[0].split()
    runtim = len(line)
    tot = 0
    if signalName not in line:
        print("Option not available")
        return 0
    sigval = line.index(signalName)
    i = 2
    counter = 0
    while i < runtim + 2:
        hold = loadFile()[i].split()[sigval+1]
        tot += float(hold)
        i += 1
        counter += 1
    avg = tot / (counter)
    avg = round(avg, 2)
    #line0 = loadFile()[2].split()[1]
    return avg


def getAverageByDay(day):
    dev = 0
    line = loadFile()[2:]
    x = []
    added = 0
    if day not in line:
        print("Option not available")
        return 0
    for i in line:
        x.append(i.split()[0])
    dayval = x.index(day)
    tot = line[dayval].split()[1:]
    dev = len(tot)
    for j in tot:
        added += float(j)
    avg = added/dev
    avg = round(avg, 2)
    return avg



def split(l, n):
    ans = []
    runtim = len(l)
    if(runtim == 0):
        print("Input error")
        return 0
    i = 0
    counter = 0
    while i < runtim:
        cutout = l[i:i+n]
        ans.append(cutout)
        i += n
    return ans




def getPalindromes():
    runtim = 1000
    i = 100
    j = 100
    pals = []

    for i in range(100,1000):
        for j in range(100, 1000):
            propal = (i * j)
            if (len(str(propal)) == 6):
                propal = str(propal)

                test = propal[::-1]
                if propal == test:
                    pals.append(propal)
    palins=list(set(pals))
    palins = sorted(palins)
    return palins

def getWords(sentence, c):
    i = 0
    counter = len(sentence)
    if(counter == 0):
        print("Input error")
        return 0
    ans = []
    sample = sentence.split()
    sample = list(set(sample))
    for i in sample:
        if c in i[0]:
            ans.append(i)
    return ans

def getCumulativeSum():
    i = 0
    counter = 1
    sum = 0
    ans = []
    for counter in range(2,101):
        while i < counter:
            sum += i
            i += 1
        ans.append(sum)
    return ans

def transpose(mat):
    runtim = len(mat)
    run2 = len(mat[0])
    ans = []
    row = []
    counter = 0
    counted = 0
    for i in range(runtim):
        for j in range(run2):
            row.append(mat[i][j])
    for i in range(run2):
        ans.append([])
        for j in range(runtim):
            ans[counted].append(row[counter])
            counter += 1
        counted += 1
    return ans

def partition(stream):
    #split a binary list into a list of 1's and 0's multiple times
    length = len(stream)
    flow = list(stream)
    counter = 0
    ans = []
    ans.append([])
    for i in range(1,length):
        if flow[i] != flow[i-1]:
            ans[counter] += flow[i - 1];
            counter += 1
            ans.append([])
        else:
            ans[counter] += flow[i];
    if(ans[counter]):
        ans[counter] += ans[counter][0]
    else:
        ans[counter] += ans[counter-2][0]
    return ans

def getTheSolution():
    pass

if __name__ == "__main__":
    signalName = "T1"
    output = getAverageBySignal(signalName)
    print(output)