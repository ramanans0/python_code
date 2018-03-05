#! /usr/local/bin/python3.4
import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.setDisabled(True)
        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        self.btnLoad.setDisabled(False)
        self.chkGraduate.stateChanged.connect(self.words)
        self.cboCollege.activated.connect(self.words)
        self.btnClear.clicked.connect(self.cleared)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.saveData)
        self.txtComponentName_1.textChanged.connect(self.words)
        self.txtComponentName_2.textChanged.connect(self.words)
        self.txtComponentName_3.textChanged.connect(self.words)
        self.txtComponentName_4.textChanged.connect(self.words)
        self.txtComponentName_5.textChanged.connect(self.words)
        self.txtComponentName_6.textChanged.connect(self.words)
        self.txtComponentName_7.textChanged.connect(self.words)
        self.txtComponentName_8.textChanged.connect(self.words)
        self.txtComponentName_9.textChanged.connect(self.words)
        self.txtComponentName_10.textChanged.connect(self.words)
        self.txtComponentName_11.textChanged.connect(self.words)
        self.txtComponentName_12.textChanged.connect(self.words)
        self.txtComponentName_13.textChanged.connect(self.words)
        self.txtComponentName_14.textChanged.connect(self.words)
        self.txtComponentName_15.textChanged.connect(self.words)
        self.txtComponentName_16.textChanged.connect(self.words)
        self.txtComponentName_17.textChanged.connect(self.words)
        self.txtComponentName_18.textChanged.connect(self.words)
        self.txtComponentName_19.textChanged.connect(self.words)
        self.txtComponentName_20.textChanged.connect(self.words)
        self.txtComponentCount_1.textChanged.connect(self.words)
        self.txtComponentCount_2.textChanged.connect(self.words)
        self.txtComponentCount_3.textChanged.connect(self.words)
        self.txtComponentCount_4.textChanged.connect(self.words)
        self.txtComponentCount_5.textChanged.connect(self.words)
        self.txtComponentCount_6.textChanged.connect(self.words)
        self.txtComponentCount_7.textChanged.connect(self.words)
        self.txtComponentCount_8.textChanged.connect(self.words)
        self.txtComponentCount_9.textChanged.connect(self.words)
        self.txtComponentCount_10.textChanged.connect(self.words)
        self.txtComponentCount_11.textChanged.connect(self.words)
        self.txtComponentCount_12.textChanged.connect(self.words)
        self.txtComponentCount_13.textChanged.connect(self.words)
        self.txtComponentCount_14.textChanged.connect(self.words)
        self.txtComponentCount_15.textChanged.connect(self.words)
        self.txtComponentCount_16.textChanged.connect(self.words)
        self.txtComponentCount_17.textChanged.connect(self.words)
        self.txtComponentCount_18.textChanged.connect(self.words)
        self.txtComponentCount_19.textChanged.connect(self.words)
        self.txtComponentCount_20.textChanged.connect(self.words)
        self.txtStudentName.textChanged.connect(self.words)
        self.txtStudentID.textChanged.connect(self.words)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        with open(filePath, "r") as signalFile:
            nameline = signalFile.readlines()[2:5]
        with open(filePath, "r") as signalFile:
            dataline = signalFile.readlines()[6:]
        #name1 = re.findall(r"\<StudentName graduate\=\"([a-z]+)\"\>([\s\w])\<\/StudentName\>", nameline[0], re.X | re.I)
        stugrad = re.findall(r"\"([a-z]+)\"", nameline[0], re.X | re.I)
        if str(stugrad[0]) == "true":
            self.chkGraduate.setChecked(True)
        elif str(stugrad[0]) == "false":
            self.chkGraduate.setChecked(False)
        stuname = re.findall(r"\>([\w\s]+)\<\/StudentName\>", nameline[0], re.X | re.I)
        self.txtStudentName.setText(str(stuname[0]))
        stuid = re.findall(r"\<StudentID\>([-\w]+)\<\/StudentID\>", nameline[1], re.X | re.I)
        self.txtStudentID.setText(str(stuid[0]))
        stucol = re.findall(r"\<College\>([\w\s]+)\<\/College\>", nameline[2], re.X | re.I)
        index = self.cboCollege.findText(str(stucol[0]))
        self.cboCollege.setCurrentIndex(index)
        #stucol = name3.group(1)
        setvals = []
        dataname = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3, self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,self.txtComponentName_10,self.txtComponentName_11,self.txtComponentName_12,self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,self.txtComponentName_19,self.txtComponentName_20]
        datanum = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3, self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,self.txtComponentCount_10,self.txtComponentCount_11,self.txtComponentCount_12,self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,self.txtComponentCount_19,self.txtComponentCount_20]
        counter = 0
        for data in dataline:
            stupro = re.findall(r"name=\"([\w\s-]+)\"", data, re.X | re.I)
            if counter < 20 and len(stupro) > 0:
                stupro = re.findall(r"name=\"([\w\s-]+)\"", data, re.X | re.I)
                dataname[counter].setText(str(stupro[0]))
                stunum = re.findall(r"count=\"([0-9]+)\"", data, re.X | re.I)
                datanum[counter].setText(str(stunum[0]))
                counter += 1

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def cleared(self):

        self.txtComponentName_1.clear()
        self.txtComponentName_2.clear()
        self.txtComponentName_3.clear()
        self.txtComponentName_4.clear()
        self.txtComponentName_5.clear()
        self.txtComponentName_6.clear()
        self.txtComponentName_7.clear()
        self.txtComponentName_8.clear()
        self.txtComponentName_9.clear()
        self.txtComponentName_10.clear()
        self.txtComponentName_11.clear()
        self.txtComponentName_12.clear()
        self.txtComponentName_13.clear()
        self.txtComponentName_14.clear()
        self.txtComponentName_15.clear()
        self.txtComponentName_16.clear()
        self.txtComponentName_17.clear()
        self.txtComponentName_18.clear()
        self.txtComponentName_19.clear()
        self.txtComponentName_20.clear()
        self.txtComponentCount_1.clear()
        self.txtComponentCount_2.clear()
        self.txtComponentCount_3.clear()
        self.txtComponentCount_4.clear()
        self.txtComponentCount_5.clear()
        self.txtComponentCount_6.clear()
        self.txtComponentCount_7.clear()
        self.txtComponentCount_8.clear()
        self.txtComponentCount_9.clear()
        self.txtComponentCount_10.clear()
        self.txtComponentCount_11.clear()
        self.txtComponentCount_12.clear()
        self.txtComponentCount_13.clear()
        self.txtComponentCount_14.clear()
        self.txtComponentCount_15.clear()
        self.txtComponentCount_16.clear()
        self.txtComponentCount_17.clear()
        self.txtComponentCount_18.clear()
        self.txtComponentCount_19.clear()
        self.txtComponentCount_20.clear()


        self.txtStudentName.clear()
        self.txtStudentID.clear()
        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        self.btnSave.setDisabled(True)
        self.btnLoad.setDisabled(False)

    def words(self):
        self.btnSave.setDisabled(False)
        self.btnLoad.setDisabled(True)

    def saveData(self):
        dataname = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3, self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,self.txtComponentName_10,self.txtComponentName_11,self.txtComponentName_12,self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,self.txtComponentName_19,self.txtComponentName_20]
        datanum = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3, self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,self.txtComponentCount_10,self.txtComponentCount_11,self.txtComponentCount_12,self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,self.txtComponentCount_19,self.txtComponentCount_20]
        with open("target.xml", "w") as outFile:
            outFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            outFile.write("<Content>\n")
            if self.chkGraduate.isChecked():
                outFile.write("    <StudentName graduate=\"{0}\">{1}</StudentName>\n".format("true",self.txtStudentName.text()))
            else:
                outFile.write("    <StudentName graduate=\"{0}\">{1}</StudentName>\n".format("false",self.txtStudentName.text()))
            outFile.write("    <StudentID>{0}</StudentID>\n".format(self.txtStudentID.text()))
            outFile.write("    <College>{0}</College>\n".format(self.cboCollege.currentText()))
            outFile.write("    <Components>\n")
            for i in range(0,20):
                temp = dataname[i].text()
                if len(temp) > 0:
                    outFile.write("        <Component name=\"{0}\" count=\"{1}\" />\n".format(dataname[i].text(), datanum[i].text()))
            outFile.write("    </Components>\n")
            outFile.write("</Content>")

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
