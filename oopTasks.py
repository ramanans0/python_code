#! /usr/local/bin/python3.4
import sys

class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        self.experimentNo=experimentNo
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = unitCount
        self.unitCost = unitCost
        self.totalCost = round(unitCount * unitCost, 2)

    def __str__(self):
        day = "{0:03d}".format(self.experimentNo)
        amount = "{0:06.2f}".format(self.totalCost)
        anser = day + ", " + self.experimentDate + ", $" + amount + ": " + self.virusName
        return anser


class Technician:

    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def __str__(self):
        num = len(self.experiments.keys())
        anser = self.techID + ", " + self.techName + ": " + "{0:02d}".format(num) + " Experiments"
        return anser

    def addExperiment(self, experiment):
        temp = experiment.experimentNo
        if temp in self.experiments.keys():
            val = self.experiments
            val[temp] = experiment
            self.experiments = val
        else:
            val = self.experiments
            val[temp] = experiment
            self.experiments = val


    def getExperiment(self, expNo):
        if expNo in self.experiments.keys():
            return self.experiments[expNo]
        else:
            return None


    def loadExperimentsFromFile(self, fileName):
        total = []
        with open(fileName, "r") as signalFile:
            lines = signalFile.readlines()[2:]
        lines.sort()
        for i in lines:
            data = i.split()
            data[0] = int(data[0])
            data[3] = int(data[3])
            data[4] = data[4].strip('$')
            data[4] = float(data[4])
            total.append(data)
        for set in total:
            abs = Experiment(*set)
            self.experiments[abs.experimentNo] = abs
        return total


    def generateTechActivity(self):
        fileName = "report "+ self.techID +".txt"
        answer = self.loadExperimentsFromFile(fileName)
        restring = self.techID + ", " + self.techName
        for set in answer:
            abs = Experiment(*set)
            #self.experiments[abs.experimentNo] = abs
            restring = restring + "\n" + str(abs)
        return restring



class Laboratory:

    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}

    def __str__(self):
        num = len(self.technicians.keys())
        restring = self.labName + ": " + "{0:02d}".format(num) + " Technicians"
        ans = []
        for set in self.technicians.values():
            # self.experiments[abs.experimentNo] = abs
            ans.append(str(set))
        ans.sort()
        for i in ans:
            restring = restring + "\n" + i
        return restring

    def addTechnician(self, technician):
        temp = technician.techName
        if temp in self.technicians.keys():
            val = self.technicians
            val[temp] = technician
            self.technicians = val
        else:
            val = self.technicians
            val[temp] = technician
            self.technicians = val

    def getTechnicians(self, *args):
        ans = []
        for arg in args:
            temp = Technician(arg)
            ans.append(temp)
        return ans

    def generateLabActivity(self):
        restring = ""
        for set in self.technicians.values():
            exp = set.generateTechActivity()
            # self.experiments[abs.experimentNo] = abs
            restring = restring + exp+ "\n\n"
        return restring[:-2]


if __name__ == "__main__":
    strings = Technician("Irene", "69069-29232")
    val = strings.generateTechActivity()
    print(str(strings))