from PyQt5 import QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox
import logging
import config


class SystemTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        self.parent = parent
        self.icon = QtGui.QIcon("app/static/icon.png")
        QSystemTrayIcon.__init__(self, self.icon, parent)
        menu = QMenu(parent)
        menu.addAction(config.applicatin_show_name, self.show_main_window)
        menu.addSeparator()
        menu.addAction('www', self.parent.open_web_site)
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
            exit()
        else:
            self.parent.hide()

    def show_main_window(self):
        self.parent.show()
