# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\temp\py\GUI\autotest_ecutest4.5\Error.ui'
#
# Created: Fri Jan 04 10:11:33 2019
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

class Ui_ErrorDgl(object):
    def setupUi(self, ErrorDgl):
        ErrorDgl.setObjectName(_fromUtf8("ErrorDgl"))
        ErrorDgl.resize(325, 110)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Error/error_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ErrorDgl.setWindowIcon(icon)
        ErrorDgl.setStyleSheet(_fromUtf8(""))
        self.label = QtGui.QLabel(ErrorDgl)
        self.label.setGeometry(QtCore.QRect(90, 30, 121, 41))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 24pt \"Arial\";"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ErrorDgl)
        QtCore.QMetaObject.connectSlotsByName(ErrorDgl)

    def retranslateUi(self, ErrorDgl):
        ErrorDgl.setWindowTitle(_translate("ErrorDgl", "Error", None))
        self.label.setText(_translate("ErrorDgl", "Error !", None))

import error_rc
