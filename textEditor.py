import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TextEditor(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.createTextEditor()
        self.fileName = ""
        self.saved = True
        self.textChanged.connect(self.textChangedEvent)

    def createTextEditor(self):
        self.setPlainText("")

    def textChangedEvent(self):
        print('Text Changed Event !')
        self.saved = False
        self.parent.barreStatu.showMessage(self.fileName + " (unsaved)")

    def openFile(self):
        print('Open File')
        # self.file = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        # open txt or html
        self.file = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;HTML Files (*.html)")
        # get file extension
        self.fileExtension = self.file[0].split(".")[-1]
        self.fileName = self.file[0]
        print(self.file)
        print(self.fileName)
        print(self.fileExtension)

        if self.fileName != "":
            if self.fileExtension == "html":
                file = open(self.fileName, "r")
                self.setHtml(file.read())
                file.close()
            else:
                file = open(self.fileName, "r")
                self.setPlainText(file.read())
                file.close()
            self.parent.barreStatu.showMessage(self.fileName)
        self.parent.centralWidget.saved = True

    def saveFile(self):
        print('File Saved')
        if self.fileName == "":
            self.saveAsFile()
        else:
            file = open(self.fileName, "w")
            file.write(self.toPlainText())
            file.close()
            self.parent.barreStatu.showMessage(self.fileName)
        self.parent.centralWidget.saved = True

    def saveAsFile(self):
        print('Save AsFile')
        self.fileName = QFileDialog.getSaveFileName(
            self.parent, "Save File", "", "All Files (*)")[0]
        if self.fileName != "":
            file = open(self.fileName, "w")
            file.write(self.toPlainText())
            file.close()
            self.parent.barreStatu.showMessage(self.fileName)

    def newFile(self):
        print('New File')
        if self.toPlainText() != "":
            msg = QMessageBox()
            msg.setText("Do you want to save the current file?")
            msg.setStandardButtons(
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Save)
            ret = msg.exec_()
            if ret == QMessageBox.Save:
                self.saveFile()
            elif ret == QMessageBox.Cancel:
                return
        self.fileName = ""
        self.setPlainText("")

