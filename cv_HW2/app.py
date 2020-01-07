# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 293)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 240, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(19, 19, 181, 101))
        self.groupBox.setObjectName("groupBox")
        self.disparity = QtWidgets.QPushButton(self.groupBox)
        self.disparity.setGeometry(QtCore.QRect(20, 30, 141, 41))
        self.disparity.setObjectName("disparity")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 20, 141, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.keypoints = QtWidgets.QPushButton(self.groupBox_2)
        self.keypoints.setGeometry(QtCore.QRect(10, 30, 121, 41))
        self.keypoints.setObjectName("keypoints")
        self.keypoints2 = QtWidgets.QPushButton(self.groupBox_2)
        self.keypoints2.setGeometry(QtCore.QRect(10, 110, 121, 41))
        self.keypoints2.setObjectName("keypoints2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 130, 181, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ncc = QtWidgets.QPushButton(self.groupBox_3)
        self.ncc.setGeometry(QtCore.QRect(20, 40, 141, 41))
        self.ncc.setObjectName("ncc")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "1. Stereo"))
        self.disparity.setText(_translate("Dialog", "1.1 Disparity"))
        self.groupBox_2.setTitle(_translate("Dialog", "3. SIFT"))
        self.keypoints.setText(_translate("Dialog", "3.1 Keypoints"))
        self.keypoints2.setText(_translate("Dialog", "3.2 Matched keypoints"))
        self.groupBox_3.setTitle(_translate("Dialog", "2. Normalized Cross Correlation"))
        self.ncc.setText(_translate("Dialog", "2.1 NCC"))
