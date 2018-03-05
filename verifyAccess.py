#! /usr/local/bin/python3.4
import sys
import collections
from collections import OrderedDict

def Users():
    with open("AccessCards.txt", "r") as signalFile:
        lines = signalFile.readlines()
    return lines

def Permissions():
    with open("Permissions.txt", "r") as testFile:
        lines = testFile.readlines()
    return lines
def AcLog():
    with open("AccessLog.txt", "r") as testFile:
        lines = testFile.readlines()
    return lines

def getUserPermissions():
    lines  = Users()
    vals = lines[2:-1]
    people = {}
    for i in vals:
        (key, val) = i.split("|")
        key = key.strip()
        val = val.strip()
        people[key] = val

    liner = Permissions()
    test = liner[2:]
    permis = []
    codes = []
    for j in test:
        j=j.strip()
        (key, val) = j.split(" - ")
        key = key.strip()
        val = val.strip()
        codes.append(key)
        permis.append(val)
    runtime = len(codes)
    userperm = {}
    i = 0
    for i in range(runtime):
        ans = ([name for name, less in people.items() if less == codes[i]])
        ans = ans[0]
        if not userperm.get(ans):
            x = set()
            x.add(permis[i])
            userperm[ans] = x
        else:
            x = userperm[ans]
            x.add(permis[i])

            userperm[ans] = x
    sorted(userperm.values())
    return userperm

def getFloorPermissions():
    lines  = Users()
    vals = lines[2:-1]
    people = {}
    for i in vals:
        (key, val) = i.split("|")
        key = key.strip()
        val = val.strip()
        people[key] = val

    liner = Permissions()
    test = liner[2:]
    permis = []
    codes = []
    for j in test:
        j=j.strip()
        (key, val) = j.split(" - ")
        key = key.strip()
        val = val.strip()
        codes.append(key)
        permis.append(val)
    runtime = len(codes)
    userperm = {}
    i = 0

    for i in range(runtime):
        ans = str(permis[i])
        anset = ([name for name, less in people.items() if less == codes[i]])
        anset = anset[0]
        if not userperm.get(ans):
            x = set()
            x.add(anset)
            userperm[ans] = x
        else:
            x = userperm[ans]
            x.add(anset)
            userperm[ans] = x
    sorted(userperm.values())
    return userperm


def getFloorRooms():
    lines = AcLog()
    access = {}
    val = []
    for i in lines:
        (key, temp) = i.split(" - ")
        temp = temp.strip()
        val.append(temp)
    runtime = len(val)
    i = 0
    key = []
    value = []
    for i in val:
        (temp1, temp2) = i.split("-")
        key.append(temp1)
        value.append(temp2)
    runs= len(key)
    sol = {}
    j = 0
    for j in range(runs):
        ans = str(key[j])
        anset = str(value[j])
        if not sol.get(ans):
            x = set()
            x.add(anset)
            sol[ans] = x
        else:
            x = sol[ans]
            x.add(anset)
            sol[ans] = x
    sorted(sol.values())
    return sol



def isAccessGrantedFor(userName, attempt):
    getDict = checkAttempts()
    check = False
    for attempts in getDict:
        if userName == attempts[0] and attempt[0] == attempts[1] and attempt[1] == attempts[2]:
            check = attempts[3]
    return check


def checkAttempts():

    lines = Users()
    usernames = lines[2:-1]
    people = {}
    for i in usernames:
        (key, val) = i.split("|")
        key = key.strip()
        val = val.strip()
        people[key] = val
    liner = AcLog()
    val = []
    names = []
    for i in liner:
        (keys, temp) = i.split(" - ")
        keys = keys.strip()
        names.append(keys)
        temp = temp.strip()
        val.append(temp)
    i = 0
    key = []
    value = []
    for i in val:
        (temp1, temp2) = i.split("-")
        key.append(temp1)
        value.append(temp2)
    runs = len(key)
    sol = []
    j = 0
    testing = getFloorPermissions()
    for j in range(runs):
        usename = [name for name, less in people.items() if less == names[j]]
        usename = usename[0]
        ans = str(key[j])
        anset = str(value[j])
        if usename in testing[ans]:
            sol.append(((usename), ans, anset, True))
        else:
            sol.append(((usename), ans, anset, False))
    return sol



def getAttemptsOf(userName):
    getDict = checkAttempts()
    sol = []
    for attempts in getDict:
        if userName in attempts:
            x = (attempts[1], attempts[2], attempts[3])
            sol.append(x)
    return sol


def getUserAttemptSummary():
    countTr = 0
    countFs = 0
    getDict = checkAttempts()
    sol = {}
    ans = {}
    for attempts in getDict:
        if attempts[0] in sol:
            x = sol[attempts[0]]
            if attempts[3] == True:
                x[0] += 1
            elif attempts[3] == False:
                x[1] += 1
            sol[attempts[0]] = x
        else:
            x = [0,0]
            if attempts[3] == True:
                x[0] += 1
            elif attempts[3] == False:
                x[1] += 1
            sol[attempts[0]] = x
    for (key, val) in sol.items():
        ans[key] = (val[0],val[1])
    return ans


def getFloorAttemptSummary():
    getDict = checkAttempts()
    sol = {}
    ans = {}
    for attempts in getDict:
        if attempts[1] in sol:
            x = sol[attempts[1]]
            if attempts[3] == True:
                x[0] += 1
            elif attempts[3] == False:
                x[1] += 1
            sol[attempts[1]] = x
        else:
            x = [0, 0]
            if attempts[3] == True:
                x[0] += 1
            elif attempts[3] == False:
                x[1] += 1
            sol[attempts[1]] = x
    for (key, val) in sol.items():
        ans[key] = (val[0], val[1])
    return ans


def getRoomAttemptSummary():
    pass

if __name__ == "__main__":
    userName = 'Gray, Tammy'
    attempt = ('Equipments', 'Room86')
    print(getFloorAttemptSummary())