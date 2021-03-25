# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\temp\py\GUI\autotest_ecutest4.5\MainCreate.ui'
#
# Created: Fri Feb 22 14:23:20 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainCreateMw(object):
    def setupUi(self, MainCreateMw):
        MainCreateMw.setObjectName(_fromUtf8("MainCreateMw"))
        MainCreateMw.resize(1141, 835)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("timgCADXKVUY.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainCreateMw.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainCreateMw)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonStart = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(400, 220, 93, 49))
        self.pushButtonStart.setStyleSheet(_fromUtf8("font: 20pt \"Agency FB\";"))
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.pushButtonStop = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(590, 220, 93, 49))
        self.pushButtonStop.setStyleSheet(_fromUtf8("font: 20pt \"Agency FB\";"))
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.pushButtonClear = QtGui.QPushButton(self.centralwidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(760, 220, 93, 49))
        self.pushButtonClear.setStyleSheet(_fromUtf8("font: 20pt \"Agency FB\";"))
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 330, 1101, 451))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(224, 255, 224);\n"
"font: 10pt \"Arial\";"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 41, 1091, 134))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditTSPath = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditTSPath.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"Agency FB\";"))
        self.lineEditTSPath.setObjectName(_fromUtf8("lineEditTSPath"))
        self.horizontalLayout.addWidget(self.lineEditTSPath)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdita2lPath = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdita2lPath.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"Agency FB\";"))
        self.lineEdita2lPath.setObjectName(_fromUtf8("lineEdita2lPath"))
        self.horizontalLayout.addWidget(self.lineEdita2lPath)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEditModelmap = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditModelmap.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"Agency FB\";"))
        self.lineEditModelmap.setObjectName(_fromUtf8("lineEditModelmap"))
        self.horizontalLayout_2.addWidget(self.lineEditModelmap)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEditUsermap = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditUsermap.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"Agency FB\";"))
        self.lineEditUsermap.setObjectName(_fromUtf8("lineEditUsermap"))
        self.horizontalLayout_4.addWidget(self.lineEditUsermap)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEditCreatetype = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCreatetype.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"Agency FB\";"))
        self.lineEditCreatetype.setObjectName(_fromUtf8("lineEditCreatetype"))
        self.horizontalLayout_6.addWidget(self.lineEditCreatetype)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEditHILType = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditHILType.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"font: 10pt \"Agency FB\";"))
        self.lineEditHILType.setObjectName(_fromUtf8("lineEditHILType"))
        self.horizontalLayout_5.addWidget(self.lineEditHILType)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 1111, 191))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("border-color: rgb(255, 255, 0);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        MainCreateMw.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainCreateMw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1141, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuNew_Style = QtGui.QMenu(self.menubar)
        self.menuNew_Style.setObjectName(_fromUtf8("menuNew_Style"))
        self.menuOld_Style = QtGui.QMenu(self.menubar)
        self.menuOld_Style.setObjectName(_fromUtf8("menuOld_Style"))
        MainCreateMw.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainCreateMw)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainCreateMw.setStatusBar(self.statusbar)
        self.ActNewOpen = QtGui.QAction(MainCreateMw)
        self.ActNewOpen.setObjectName(_fromUtf8("ActNewOpen"))
        self.ActCreateDB = QtGui.QAction(MainCreateMw)
        self.ActCreateDB.setObjectName(_fromUtf8("ActCreateDB"))
        self.menuNew_Style.addAction(self.ActNewOpen)
        self.menuOld_Style.addAction(self.ActCreateDB)
        self.menubar.addAction(self.menuNew_Style.menuAction())
        self.menubar.addAction(self.menuOld_Style.menuAction())

        self.retranslateUi(MainCreateMw)
        QtCore.QMetaObject.connectSlotsByName(MainCreateMw)

    def retranslateUi(self, MainCreateMw):
        MainCreateMw.setWindowTitle(_translate("MainCreateMw", "Auto Create 4.5", None))
        self.pushButtonStart.setText(_translate("MainCreateMw", "Start", None))
        self.pushButtonStop.setText(_translate("MainCreateMw", "Stop", None))
        self.pushButtonClear.setText(_translate("MainCreateMw", "Clear", None))
        self.label.setText(_translate("MainCreateMw", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Testcase Path:</span></p></body></html>", None))
        self.label_3.setText(_translate("MainCreateMw", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">A2L Path:</span></p></body></html>", None))
        self.label_4.setText(_translate("MainCreateMw", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Model Map:</span></p></body></html>", None))
        self.label_5.setText(_translate("MainCreateMw", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">User Map:</span></p></body></html>", None))
        self.label_6.setText(_translate("MainCreateMw", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Create Type:</span></p></body></html>", None))
        self.label_2.setText(_translate("MainCreateMw", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">HIL Type:</span></p></body></html>", None))
        self.groupBox.setTitle(_translate("MainCreateMw", "Information", None))
        self.menuNew_Style.setTitle(_translate("MainCreateMw", "Create Pkg", None))
        self.menuOld_Style.setTitle(_translate("MainCreateMw", "Create DB", None))
        self.ActNewOpen.setText(_translate("MainCreateMw", "Open", None))
        self.ActNewOpen.setShortcut(_translate("MainCreateMw", "Ctrl+C", None))
        self.ActCreateDB.setText(_translate("MainCreateMw", "Open", None))

import xiaoniao_rc
