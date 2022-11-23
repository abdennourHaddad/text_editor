import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append("./textEditor.py")
from textEditor import * 

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor")
        self.resize(1000, 900)
        self.show()

        # create Actions
        self.createActions()

        # create menu bar
        self.createMenuBar()

        # create toolbar
        self.createToolBars()

        # create status bar
        self.barreStatu = self.statusBar()
        self.barreStatu.showMessage('Ready')

        # create a text editor
        self.centralWidget = TextEditor(self)
        self.setCentralWidget(self.centralWidget)

        # close event
        self.unsaved = self.centralWidget.saved
        #self.closeEvent = self.closeEvent
        # self.closeEvent = self.closeEvent(self)

    # create the actions

    def createActions(self):
        # Create New action
        self.newAction = QAction(QIcon('images/new.png'), '&New', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setToolTip('New file')
        self.newAction.setStatusTip('New File')
        self.newAction.triggered.connect(self.newFile)

        # Create Open action
        self.openAction = QAction(QIcon('images/open.png'), '&Open', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setToolTip('Open file')
        self.openAction.setStatusTip('Open File')
        self.openAction.triggered.connect(self.openFile)

        # Create Save action
        self.saveAction = QAction(QIcon('images/save.png'), '&Save', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setToolTip('Save file')
        self.saveAction.setStatusTip('Save File')
        self.saveAction.triggered.connect(self.saveFile)

        # Create Cut action
        self.cutAction = QAction(QIcon('images/cut.png'), '&Copy', self)
        self.cutAction.setShortcut('Ctrl+X')
        self.cutAction.setToolTip('Cut')
        self.cutAction.setStatusTip('Cut')
        self.cutAction.triggered.connect(self.cutCall)

        # Create Copy action
        self.copyAction = QAction(QIcon('images/copy.png'), '&Copy', self)
        self.copyAction.setShortcut('Ctrl+C')
        self.copyAction.setToolTip('Copy')
        self.copyAction.setStatusTip('Copy')
        self.copyAction.triggered.connect(self.copyCall)

        # Create Paste action
        self.pasteAction = QAction(QIcon('images/paste.png'), '&Paste', self)
        self.pasteAction.setShortcut('Ctrl+V')
        self.pasteAction.setToolTip('Paste')
        self.pasteAction.setStatusTip('Paste')
        self.pasteAction.triggered.connect(self.pasteCall)

        # Create Exit action
        self.exitAction = QAction(QIcon('images/quit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        # La méthode close est directement fournie par la classe QMainWindow.
        self.exitAction.triggered.connect(self.close)

    # create the menu bar

    def createMenuBar(self):
        menuBar = self.menuBar()  # initialise the menu bar
        self.setMenuBar(menuBar)

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.openAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.cutAction)
        fileMenu.addAction(self.copyAction)
        fileMenu.addAction(self.pasteAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

    # create the tool bar

    def createToolBars(self):
        fileToolBar = self.addToolBar("File tool bar")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addSeparator()
        fileToolBar.addAction(self.openAction)
        fileToolBar.addSeparator()
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addSeparator()
        fileToolBar.addAction(self.cutAction)
        fileToolBar.addAction(self.copyAction)
        fileToolBar.addAction(self.pasteAction)
        fileToolBar.addSeparator()
        fileToolBar.addAction(self.exitAction)

    # connect the slots
    def saveFile(self):
        self.centralWidget.saveFile()

    def newFile(self):
        self.centralWidget.newFile()

    def openFile(self):
        self.centralWidget.openFile()

    def cutCall(self):
        print('Cut')

    # @pyqtSlot()
    def copyCall(self):
        print('Copy')

    # @pyqtSlot()
    def pasteCall(self):
        print('Paste')

    # @pyqtSlot()
    def exitCall(self):
        print('Exit app')

    # @pyqtSlot()
    def clickMethod(self):
        print('PyQt')

    def closeEvent(self, event):
        event.ignore()
        reply = QMessageBox.question(
            self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes :
            # if this file is unsaved
            if self.centralWidget.saved == False :
                reply = QMessageBox.question(
                    self, 'Message', "Do you want to save the file?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.centralWidget.saveFile()

            import sys
            sys.exit()
        else :
            event.ignore()

