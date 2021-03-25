# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\temp\py\GUI\autotest_ecutest4.5\Progress.ui'
#
# Created: Wed Feb 27 16:35:51 2019
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

class Ui_ProgressDlg(object):
    def setupUi(self, ProgressDlg):
        ProgressDlg.setObjectName(_fromUtf8("ProgressDlg"))
        ProgressDlg.resize(762, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressDlg.sizePolicy().hasHeightForWidth())
        ProgressDlg.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/xiaoniao/timgCADXKVUY.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProgressDlg.setWindowIcon(icon)
        self.progressBar = QtGui.QProgressBar(ProgressDlg)
        self.progressBar.setGeometry(QtCore.QRect(120, 40, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(ProgressDlg)
        self.label.setGeometry(QtCore.QRect(250, 10, 121, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ProgressDlg)
        QtCore.QMetaObject.connectSlotsByName(ProgressDlg)

    def retranslateUi(self, ProgressDlg):
        ProgressDlg.setWindowTitle(_translate("ProgressDlg", "Please Wait", None))
        self.label.setText(_translate("ProgressDlg", "Generating....", None))

import xiaoniao_rc
