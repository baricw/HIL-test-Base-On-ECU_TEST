# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\temp\py\GUI\autotest_ecutest4.5\Matrix.ui'
#
# Created: Wed Feb 20 14:33:10 2019
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

class Ui_MatrixDlg(object):
    def setupUi(self, MatrixDlg):
        MatrixDlg.setObjectName(_fromUtf8("MatrixDlg"))
        MatrixDlg.resize(706, 469)
        self.line_3 = QtGui.QFrame(MatrixDlg)
        self.line_3.setGeometry(QtCore.QRect(10, 100, 651, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.textBrowserinsert = QtGui.QTextBrowser(MatrixDlg)
        self.textBrowserinsert.setGeometry(QtCore.QRect(20, 250, 661, 201))
        self.textBrowserinsert.setStyleSheet(_fromUtf8("font: 7pt \"Arial\";"))
        self.textBrowserinsert.setObjectName(_fromUtf8("textBrowserinsert"))
        self.line = QtGui.QFrame(MatrixDlg)
        self.line.setGeometry(QtCore.QRect(580, 20, 16, 81))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(MatrixDlg)
        self.line_2.setGeometry(QtCore.QRect(20, 210, 651, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.layoutWidget = QtGui.QWidget(MatrixDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 561, 30))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEditDBC = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditDBC.setObjectName(_fromUtf8("lineEditDBC"))
        self.horizontalLayout.addWidget(self.lineEditDBC)
        self.pushButtonDBC = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonDBC.setObjectName(_fromUtf8("pushButtonDBC"))
        self.horizontalLayout.addWidget(self.pushButtonDBC)
        self.label_2 = QtGui.QLabel(MatrixDlg)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 191, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(MatrixDlg)
        self.label.setGeometry(QtCore.QRect(20, 110, 191, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowserfile = QtGui.QTextBrowser(MatrixDlg)
        self.textBrowserfile.setGeometry(QtCore.QRect(20, 140, 651, 61))
        self.textBrowserfile.setStyleSheet(_fromUtf8("font: 7pt \"Arial\";"))
        self.textBrowserfile.setObjectName(_fromUtf8("textBrowserfile"))
        self.layoutWidget_2 = QtGui.QWidget(MatrixDlg)
        self.layoutWidget_2.setGeometry(QtCore.QRect(600, 30, 100, 67))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonGen = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButtonGen.setFont(font)
        self.pushButtonGen.setObjectName(_fromUtf8("pushButtonGen"))
        self.verticalLayout.addWidget(self.pushButtonGen)
        self.pushButtonclose = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButtonclose.setFont(font)
        self.pushButtonclose.setObjectName(_fromUtf8("pushButtonclose"))
        self.verticalLayout.addWidget(self.pushButtonclose)
        self.label_3.setBuddy(self.lineEditDBC)

        self.retranslateUi(MatrixDlg)
        QtCore.QObject.connect(self.pushButtonclose, QtCore.SIGNAL(_fromUtf8("clicked()")), MatrixDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(MatrixDlg)

    def retranslateUi(self, MatrixDlg):
        MatrixDlg.setWindowTitle(_translate("MatrixDlg", "Create DB", None))
        self.label_3.setText(_translate("MatrixDlg", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff5500;\">DBCPath:</span></p></body></html>", None))
        self.pushButtonDBC.setText(_translate("MatrixDlg", "SetPath", None))
        self.label_2.setText(_translate("MatrixDlg", "Insert Progress:", None))
        self.label.setText(_translate("MatrixDlg", "DBC and LDF File Name: ", None))
        self.pushButtonGen.setText(_translate("MatrixDlg", "Generate", None))
        self.pushButtonclose.setText(_translate("MatrixDlg", "close", None))

