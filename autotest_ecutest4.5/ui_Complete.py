# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\temp\py\GUI\autotest_ecutest4.5\Complete.ui'
#
# Created: Fri Jan 04 10:23:27 2019
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

class Ui_CompleteDgl(object):
    def setupUi(self, CompleteDgl):
        CompleteDgl.setObjectName(_fromUtf8("CompleteDgl"))
        CompleteDgl.resize(328, 110)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/haha/HaHaBundle.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CompleteDgl.setWindowIcon(icon)
        CompleteDgl.setStyleSheet(_fromUtf8(""))
        self.label = QtGui.QLabel(CompleteDgl)
        self.label.setGeometry(QtCore.QRect(70, 30, 171, 41))
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"font: 20pt \"Arial\";"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(CompleteDgl)
        QtCore.QMetaObject.connectSlotsByName(CompleteDgl)

    def retranslateUi(self, CompleteDgl):
        CompleteDgl.setWindowTitle(_translate("CompleteDgl", "Complete", None))
        self.label.setText(_translate("CompleteDgl", "Complete !", None))

import haha_rc
