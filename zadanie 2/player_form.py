from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
def setupUi(self, MainWindow):
MainWindow.setObjectName("MainWindow")
MainWindow.resize(391, 543)
self.centralwidget = QtWidgets.QWidget(MainWindow)
self.centralwidget.setObjectName("centralwidget")

self.listWidget = QtWidgets.QListWidget(self.centralwidget)
self.listWidget.setGeometry(QtCore.QRect(20, 20, 351, 181))

self.pushButton = QtWidgets.QPushButton(self.centralwidget)
self.pushButton.setGeometry(QtCore.QRect(30, 220, 331, 31))
self.pushButton.setObjectName("pushButton")
self.pushButton.setText("Start")

self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
self.pushButton_2.setGeometry(QtCore.QRect(30, 260, 331, 31))
self.pushButton_2.setObjectName("pushButton_2")
self.pushButton_2.setText("Pause")

self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
self.pushButton_3.setGeometry(QtCore.QRect(30, 300, 331, 31))
self.pushButton_3.setObjectName("pushButton_3")
self.pushButton_3.setText("Update")

self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
self.pushButton_4.setGeometry(QtCore.QRect(30, 340, 331, 31))
self.pushButton_4.setObjectName("pushButton_4")
self.pushButton_4.setText("Random")

MainWindow.setCentralWidget(self.centralwidget)

self.menubar = QtWidgets.QMenuBar(MainWindow)
self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 22))
self.menubar.setObjectName("menubar")
MainWindow.setMenuBar(self.menubar)

self.statusbar = QtWidgets.QStatusBar(MainWindow)
self.statusbar.setObjectName("statusbar")
MainWindow.setStatusBar(self.statusbar)

self.retranslateUi(MainWindow)
QtCore.QMetaObject.connectSlotsByName(MainWindow)


def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
