# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base_ui_linux.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setStyleSheet("")
        self.main_widget.setObjectName("main_widget")
        self.bottom_widget = QtWidgets.QWidget(self.main_widget)
        self.bottom_widget.setGeometry(QtCore.QRect(0, 240, 401, 41))
        self.bottom_widget.setObjectName("bottom_widget")
        self.bottom_widget_label = QtWidgets.QLabel(self.bottom_widget)
        self.bottom_widget_label.setGeometry(QtCore.QRect(10, 5, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bottom_widget_label.setFont(font)
        self.bottom_widget_label.setObjectName("bottom_widget_label")
        self.installUpdates = QtWidgets.QDialogButtonBox(self.bottom_widget)
        self.installUpdates.setGeometry(QtCore.QRect(290, 5, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(False)
        font.setWeight(50)
        self.installUpdates.setFont(font)
        self.installUpdates.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.installUpdates.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.installUpdates.setObjectName("installUpdates")
        self.action_after_widget = QtWidgets.QWidget(self.main_widget)
        self.action_after_widget.setGeometry(QtCore.QRect(-2, 180, 401, 31))
        self.action_after_widget.setObjectName("action_after_widget")
        self.action_after_time = QtWidgets.QTimeEdit(self.action_after_widget)
        self.action_after_time.setGeometry(QtCore.QRect(160, 0, 130, 24))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.action_after_time.setFont(font)
        self.action_after_time.setStyleSheet("")
        self.action_after_time.setObjectName("action_after_time")
        self.action_after_select = QtWidgets.QComboBox(self.action_after_widget)
        self.action_after_select.setGeometry(QtCore.QRect(7, 0, 110, 26))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(False)
        font.setWeight(50)
        self.action_after_select.setFont(font)
        self.action_after_select.setStyleSheet("QComboBox{selection-background-color: blue}")
        self.action_after_select.setObjectName("action_after_select")
        self.action_after_select.addItem("")
        self.action_after_select.addItem("")
        self.action_after_select.addItem("")
        self.action_after_select.addItem("")
        self.label_2 = QtWidgets.QLabel(self.action_after_widget)
        self.label_2.setGeometry(QtCore.QRect(120, 5, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.action_after_cancel = QtWidgets.QPushButton(self.action_after_widget)
        self.action_after_cancel.setGeometry(QtCore.QRect(340, 0, 60, 24))
        self.action_after_cancel.setObjectName("action_after_cancel")
        self.action_after_submit = QtWidgets.QPushButton(self.action_after_widget)
        self.action_after_submit.setGeometry(QtCore.QRect(293, 0, 45, 24))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.action_after_submit.setFont(font)
        self.action_after_submit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.action_after_submit.setStyleSheet("    QPushButton{}\n"
"QPushButton:pressed{}")
        self.action_after_submit.setObjectName("action_after_submit")
        self.action_at_widget = QtWidgets.QWidget(self.main_widget)
        self.action_at_widget.setGeometry(QtCore.QRect(-2, 210, 401, 31))
        self.action_at_widget.setObjectName("action_at_widget")
        self.action_at_select = QtWidgets.QComboBox(self.action_at_widget)
        self.action_at_select.setGeometry(QtCore.QRect(7, 0, 110, 26))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.action_at_select.setFont(font)
        self.action_at_select.setObjectName("action_at_select")
        self.action_at_select.addItem("")
        self.action_at_select.addItem("")
        self.action_at_select.addItem("")
        self.action_at_select.addItem("")
        self.label_3 = QtWidgets.QLabel(self.action_at_widget)
        self.label_3.setGeometry(QtCore.QRect(127, 5, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.action_at_submit = QtWidgets.QPushButton(self.action_at_widget)
        self.action_at_submit.setGeometry(QtCore.QRect(293, 0, 45, 24))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.action_at_submit.setFont(font)
        self.action_at_submit.setObjectName("action_at_submit")
        self.action_at_datetime = QtWidgets.QDateTimeEdit(self.action_at_widget)
        self.action_at_datetime.setGeometry(QtCore.QRect(160, 0, 130, 24))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.action_at_datetime.setFont(font)
        self.action_at_datetime.setObjectName("action_at_datetime")
        self.action_at_cancel = QtWidgets.QPushButton(self.action_at_widget)
        self.action_at_cancel.setGeometry(QtCore.QRect(340, 0, 60, 24))
        self.action_at_cancel.setObjectName("action_at_cancel")
        self.label_notification = QtWidgets.QLabel(self.main_widget)
        self.label_notification.setGeometry(QtCore.QRect(20, 150, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_notification.setFont(font)
        self.label_notification.setStyleSheet("qproperty-alignment: AlignCenter;")
        self.label_notification.setText("")
        self.label_notification.setObjectName("label_notification")
        self.upper_widget_label = QtWidgets.QLabel(self.main_widget)
        self.upper_widget_label.setGeometry(QtCore.QRect(0, 70, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.upper_widget_label.setFont(font)
        self.upper_widget_label.setStyleSheet("qproperty-alignment: AlignCenter;")
        self.upper_widget_label.setObjectName("upper_widget_label")
        self.background_widget = QtWidgets.QWidget(self.main_widget)
        self.background_widget.setGeometry(QtCore.QRect(-10, -10, 421, 291))
        self.background_widget.setStyleSheet("#background_widget{background-color: qlineargradient(spread:pad, x1:0.502, y1:0, x2:0.507, y2:1, stop:0.444976 rgba(27, 188, 155, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.background_widget.setObjectName("background_widget")
        self.background_widget.raise_()
        self.bottom_widget.raise_()
        self.action_after_widget.raise_()
        self.action_at_widget.raise_()
        self.label_notification.raise_()
        self.upper_widget_label.raise_()
        MainWindow.setCentralWidget(self.main_widget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionWqeasd = QtWidgets.QAction(MainWindow)
        self.actionWqeasd.setObjectName("actionWqeasd")
        self.actionWqe = QtWidgets.QAction(MainWindow)
        self.actionWqe.setObjectName("actionWqe")
        self.actionQwe = QtWidgets.QAction(MainWindow)
        self.actionQwe.setObjectName("actionQwe")
        self.action_settings = QtWidgets.QAction(MainWindow)
        self.action_settings.setObjectName("action_settings")
        self.action_sign_out = QtWidgets.QAction(MainWindow)
        self.action_sign_out.setObjectName("action_sign_out")
        self.action_show_all_pc = QtWidgets.QAction(MainWindow)
        self.action_show_all_pc.setObjectName("action_show_all_pc")
        self.action_faq = QtWidgets.QAction(MainWindow)
        self.action_faq.setObjectName("action_faq")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action_website = QtWidgets.QAction(MainWindow)
        self.action_website.setObjectName("action_website")
        self.action_license = QtWidgets.QAction(MainWindow)
        self.action_license.setObjectName("action_license")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_contact_us = QtWidgets.QAction(MainWindow)
        self.action_contact_us.setObjectName("action_contact_us")
        self.action_contribute = QtWidgets.QAction(MainWindow)
        self.action_contribute.setObjectName("action_contribute")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menuFile.addAction(self.action_settings)
        self.menuFile.addAction(self.action_show_all_pc)
        self.menuFile.addAction(self.action_sign_out)
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_faq)
        self.menuHelp.addAction(self.action_website)
        self.menuHelp.addAction(self.action_contact_us)
        self.menuHelp.addAction(self.action_contribute)
        self.menuHelp.addAction(self.action_about)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote PC"))
        self.bottom_widget_label.setText(_translate("MainWindow", "There are new updates.Install? "))
        self.action_after_select.setItemText(0, _translate("MainWindow", "Shutdown"))
        self.action_after_select.setItemText(1, _translate("MainWindow", "Restart"))
        self.action_after_select.setItemText(2, _translate("MainWindow", "LogOut"))
        self.action_after_select.setItemText(3, _translate("MainWindow", "Sleep"))
        self.label_2.setText(_translate("MainWindow", "after"))
        self.action_after_cancel.setText(_translate("MainWindow", "Cancel"))
        self.action_after_submit.setText(_translate("MainWindow", "OK"))
        self.action_at_select.setItemText(0, _translate("MainWindow", "Shutdown"))
        self.action_at_select.setItemText(1, _translate("MainWindow", "Restart"))
        self.action_at_select.setItemText(2, _translate("MainWindow", "LogOut"))
        self.action_at_select.setItemText(3, _translate("MainWindow", "Sleep"))
        self.label_3.setText(_translate("MainWindow", "at"))
        self.action_at_submit.setText(_translate("MainWindow", "OK"))
        self.action_at_cancel.setText(_translate("MainWindow", "Cancel"))
        self.upper_widget_label.setText(_translate("MainWindow", "Program is Running"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionWqeasd.setText(_translate("MainWindow", "FIle"))
        self.actionWqe.setText(_translate("MainWindow", "wqe"))
        self.actionQwe.setText(_translate("MainWindow", "qwe"))
        self.action_settings.setText(_translate("MainWindow", "Settings"))
        self.action_sign_out.setText(_translate("MainWindow", "Sign out"))
        self.action_show_all_pc.setText(_translate("MainWindow", "Show My PC\'s"))
        self.action_faq.setText(_translate("MainWindow", "FAQ"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.action_website.setText(_translate("MainWindow", "Web Site"))
        self.action_license.setText(_translate("MainWindow", "License"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_contact_us.setText(_translate("MainWindow", "Contact Us"))
        self.action_contribute.setText(_translate("MainWindow", "Contribute"))
        self.action_about.setText(_translate("MainWindow", "About"))

