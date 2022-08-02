# opencv imports
import cv2
import numpy as np
from matplotlib import pyplot as pyplot
import imutils

# pyqt5 imports - user interface
import sys
from PyQt5 import QtWidgets, QtCore 
from PyQt5.QtWidgets import (
    QMainWindow, QAction, 
    QApplication, QMessageBox 
)
from PyQt5.QtGui import QIcon,QImage,QPixmap

#from datetime import date, datetime
from PyQt5.QtCore import QDate, QTime, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createMenu()
        self.createStatusBar()
        self.creatToolbar()
        self.createBoxLayout()
       
    def createMenu(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        fileMenu = menuBar.addMenu("File")
        viewMenu = menuBar.addMenu("View")
        functionsMenu = menuBar.addMenu("Functions")

        openMenu = QAction(QIcon('./icons/folder.png'),"Open Image", self)
        openMenu.setShortcut("Ctrl+O")
        openMenu.setStatusTip("Open a file")
        
        # close window
        exitFunction = QAction(QIcon('./icons/exit.png'), "Exit", self)
        exitFunction.setShortcut('Ctrl+Q')
        exitFunction.setStatusTip('Exit application')
        exitFunction.triggered.connect(self.close)

        # drawMenu 
        drawLine = QAction("Draw Line", self)
        drawLine.triggered.connect(self.drawLines)
        drawCircle = QAction("Draw Circle", self)
        blurImg = QAction("Blur Image", self)
        blurImg.triggered.connect(self.blurImage)
        
        # checkable status bar
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleStatusBar)

        # associate menus to the file menu
        fileMenu.addAction(openMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitFunction)
        fileMenu.addSeparator()
        viewMenu.addAction(viewStatAct)

        # associate menu to functions menu
        drawingShapes = functionsMenu.addMenu("Drawing Shapes")
        
        # associate menu to functions menu
        drawingShapes.addAction(drawLine)
        drawingShapes.addAction(drawCircle)
        functionsMenu.addSeparator()
        functionsMenu.addAction(blurImg)
    
    def toggleStatusBar(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def createStatusBar(self):
        # date and time
        current_date = QDate.currentDate()
        current_time = QTime.currentTime()
        date = current_date.toString(Qt.ISODate)
        time = current_time.toString(Qt.DefaultLocaleLongDate)

        self.statusbar = self.statusBar()
        msg = "Status: Ready        Date: {}        Time: {}".format(date,time)
        self.statusbar.showMessage(msg)  

    def creatToolbar(self):
        toolbar1 = self.addToolBar("toolbar")
        #toolbar1.setMovable(False)
        
        openFile = QAction(QIcon('./icons/folder.png'),"Open File", self)
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.openDialogFile)
        startWebCam = QAction(QIcon('./icons/camera.png'),"Start WebCam", self)
        startWebCam.setStatusTip('Start Webcam')

        #attach the toolbar
        toolbar1.addAction(openFile)
        toolbar1.addSeparator()
        toolbar1.addAction(startWebCam)

    def createBoxLayout(self):
        self.imgLabel = QtWidgets.QLabel(self)
        self.imgLabel.setGeometry(0, 50,300,280)
        self.imgLabel.setObjectName("img_pane")
        self.imgLabel.setText("Add Image or start webcam to begin!")
        self.imgLabel.setWordWrap(True)
        self.imgLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.optlabel = QtWidgets.QLabel(self)
        self.optlabel.setGeometry(300,50,200,280)
        self.optlabel.setObjectName("opt_pane")
        self.optlabel.setText(" Welcome!")
        self.optlabel.setWordWrap(True)
        self.optlabel.setAlignment(QtCore.Qt.AlignCenter)

    def openDialogFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        self.path = fileName[0]

        if self.path:
            pixMap = QPixmap(self.path)
            self.imgLabel.setPixmap(pixMap)
            msgStatus = "Image: {} loaded successfuly!".format(self.path)
            self.statusBar().showMessage(msgStatus)

            return self.path

    def drawLines(self):
        imgPath = self.path
        theImg = cv2.imread(imgPath)
        newImg = cv2.line(theImg, (0,20),(230,350),(200,0,50),4)
        showImg = QImage(newImg.data, newImg.shape[1], newImg.shape[0], newImg.shape[1] * 3,QImage.Format_RGB888).rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(showImg))

    def blurImage(self):
        imgPath = self.path
        theImg = cv2.imread(imgPath, cv2.IMREAD_COLOR)
        newImg = cv2.blur(theImg,(5,5)) #kernel value
        showImg = QImage(newImg.data, newImg.shape[1], newImg.shape[0], newImg.shape[1] * 3,QImage.Format_RGB888).rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(showImg))
        self.optlabel.setText("Blured Image with (5,5) kernel")
    
    
    def undoText(self):
        self.imgLabel.setText("The edit menu works")
        self.optlabel.setText("Let us move on")

    def copyText(self):
        imagePath = self.path
        self.imgLabel.setText(imagePath)

    def pasteText(self):
        pass


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:            
        # in every pyqt application it is required to create the object of QApplication
        app = QtWidgets.QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))

    # initialize and show Qwidget object
    main = MainWindow()
    # main window properties
    main.setWindowTitle("Capstone Project")
    main.resize(500,350)
    main.setWindowIcon(QIcon("./icons/camus.jpg"))
    main.setMinimumSize(500,350)
    main.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")
