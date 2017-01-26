from PyQt5 import QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox, QAction
from PyQt5.QtCore import pyqtSignal
import logging
import config
import sys
from . import constants
import threading


class SystemTray(QSystemTrayIcon):
    tray_notification_signal = pyqtSignal(str,
                                          name=constants.NOTIFICATION_TRAY)

    def __init__(self, parent=None):
        self.parent = parent
        self.icon = QtGui.QIcon(config.app_icon_path)
        QSystemTrayIcon.__init__(self, self.icon, parent)
        menu = QMenu(parent)
        self.show_notification = QAction(self.parent)
        self.show_notification.setDisabled(True)
        self.show_notification.setObjectName(constants.NOTIFICATION_TRAY)
        menu.setStyleSheet("")
        menu.addAction(self.show_notification)
        menu.addSeparator()
        menu.addAction(config.applicatin_show_name, self.show_main_window)
        menu.addSeparator()
        menu.addAction('WWW', self.parent.open_web_site)
        menu.addSeparator()
        menu.addAction("Exit", self.on_exit)
        self.setContextMenu(menu)

    def on_exit(self):
        reply = QMessageBox.question(self.parent, 'Message',
                                     'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        self.parent.show()
        if reply == QMessageBox.Yes:
            logging.debug('Exit from application via tray')
            sys.exit()
        else:
            self.parent.hide()

    def show_main_window(self):
        self.parent.show()
