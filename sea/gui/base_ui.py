# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created: Wed Mar 23 12:56:13 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(Form)
        self.bottom_frame = QtWidgets.QFrame(Form)

        self.bottom_frame.setObjectName("bottom_frame")
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(self.top_frame)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.verticalLayout.addWidget(self.bottom_frame, 1)
        self.centr_frame = QtWidgets.QFrame(Form)
        self.centr_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.centr_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.centr_frame.setObjectName("centr_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centr_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_box_1 = QtWidgets.QFrame(self.centr_frame)
        # self.frame_box_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_box_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_box_1.setObjectName("frame_box_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_box_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_gamer = QtWidgets.QLabel(self.frame_box_1)
        self.label_gamer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gamer.setObjectName("label_gamer")
        self.verticalLayout_2.addWidget(self.label_gamer, 1)
        self.frame_gamer_Grid = QtWidgets.QFrame(self.frame_box_1)
        # self.frame_gamer_Grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_gamer_Grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gamer_Grid.setObjectName("frame_gamer_Grid")
        self.verticalLayout_2.addWidget(self.frame_gamer_Grid, 10)
        self.horizontalLayout_3.addWidget(self.frame_box_1)
        self.frame_box_2 = QtWidgets.QFrame(self.centr_frame)
        # self.frame_box_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_box_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_box_2.setObjectName("frame_box_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_box_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_pc = QtWidgets.QLabel(self.frame_box_2)
        self.label_pc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pc.setObjectName("label_pc")
        self.verticalLayout_4.addWidget(self.label_pc, 1)
        self.frame_pc_Grid = QtWidgets.QFrame(self.frame_box_2)
        # self.frame_pc_Grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_pc_Grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pc_Grid.setObjectName("frame_pc_Grid")
        self.verticalLayout_4.addWidget(self.frame_pc_Grid, 10)
        self.horizontalLayout_3.addWidget(self.frame_box_2)
        self.verticalLayout.addWidget(self.centr_frame, 10)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.auto_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.auto_btn.setObjectName("auto_btn")
        self.horizontalLayout.addWidget(self.auto_btn)
        self.horizontalLayout.setContentsMargins(0, 15, 0, 15)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.new_game_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.new_game_btn.setObjectName("new_game_btn")
        self.horizontalLayout.addWidget(self.new_game_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.settings_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout.addWidget(self.settings_btn)

        self.verticalLayout.addWidget(self.top_frame, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.close_btn.setText(_translate("Form", "close"))
        self.label_gamer.setText(_translate("Form", "Игрок"))
        self.label_pc.setText(_translate("Form", "Компьютер"))
        self.auto_btn.setText(_translate("Form", "auto_fleet_user"))
        self.new_game_btn.setText(_translate("Form", "new"))
        self.settings_btn.setText(_translate("Form", "set"))

