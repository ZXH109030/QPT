# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unzip.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_unzip_file_dialog(object):
    def setupUi(self, unzip_file_dialog):
        unzip_file_dialog.setObjectName("unzip_file_dialog")
        unzip_file_dialog.setEnabled(True)
        unzip_file_dialog.resize(394, 22)
        unzip_file_dialog.setMinimumSize(QtCore.QSize(394, 22))
        unzip_file_dialog.setMaximumSize(QtCore.QSize(394, 22))
        self.progressBar = QtWidgets.QProgressBar(unzip_file_dialog)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 391, 22))
        self.progressBar.setMinimumSize(QtCore.QSize(391, 22))
        self.progressBar.setMaximumSize(QtCore.QSize(391, 22))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(unzip_file_dialog)
        QtCore.QMetaObject.connectSlotsByName(unzip_file_dialog)

    def retranslateUi(self, unzip_file_dialog):
        _translate = QtCore.QCoreApplication.translate
        unzip_file_dialog.setWindowTitle(_translate("unzip_file_dialog", "初始化环境"))
