from .base_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from .callbacks_events import Callback
from PyQt5.QtCore import Qt, pyqtSignal, QDateTime, QTime, QTimer
from PyQt5 import QtGui
import config
import datetime
from utils import shelve_get, seconds_from_datetime, shelve_save, \
    format_hours_minutes_from_seconds
from app import constants
import threading
import time
import logging


class MainWindow(QMainWindow, Ui_MainWindow):
    notification_signal = pyqtSignal(str, name=constants.NOTIFICATION)
    timer_after_signal = pyqtSignal(QTime, name=constants.TIMER_AFTER)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.run_from_dt = datetime.datetime.now()
        self.setup_app()
        self.callbacks = Callback(self)
        self.on_run_app()
        tray_icon = SystemTray(self)
        tray_icon.show()

    def setup_app(self):
        logging.debug('Setting up UI application...')
        self.setupUi(self)
        logging.debug('Setting default date time for timers')
        self.action_after_time.setTime(QTime(
            *config.action_after_time_default))
        self.action_after_time.setMinimumTime(QTime(
            *config.action_after_time_minimum))
        self.action_at_datetime.setDateTime(self.run_from_dt)
        self.action_at_datetime.setMinimumDateTime(
            self.run_from_dt + datetime.timedelta(minutes=1))
        self.action_at_datetime.setMaximumDateTime(self.run_from_dt +
                                                   datetime.timedelta(7))

    def show_notification_label(self, text):
        logging.debug('Show notification label. \nText: ' % text)
        self.label_notification.setText(text)

    def on_run_app(self):
        logging.debug('Getting values from shelve for timers')
        timer_at = shelve_get(constants.TIMER_AT_DATETIME)
        timer_after = shelve_get(constants.TIMER_AFTER_TIME)
        time_now = time.time()
        if timer_at:
            logging.debug('At timer exists in shelve file. \n'
                          'Timer at time: %s' % timer_at)
            if seconds_from_datetime(timer_at) > time_now:
                logging.debug('Starting at timer gotten from shelve')
                threading.Thread(target=self.callbacks.start_timer,
                                 args=(constants.DATE_AT, timer_at,
                                       shelve_get(constants.TIMER_AT_ACTION)),
                                 daemon=True).start()
                self.callbacks.set_disabled_timer(constants.DATE_AT)

            else:
                logging.debug('Setting timer at to shelve as None')
                shelve_save(**{constants.TIMER_AT_DATETIME: None,
                               constants.TIMER_AT_ACTION: None})
        if timer_after:
            logging.debug('After timer exists in shelve file. \n'
                          'Timer after time: %s' % timer_after)
            if seconds_from_datetime(timer_after,
                                     tm_format='%m/%d/%y %H:%M %S') > \
                    time.time():
                seconds_to_action = seconds_from_datetime(
                    timer_after, tm_format='%m/%d/%y %H:%M %S') - time_now
                days_time_to_action = format_hours_minutes_from_seconds(
                    seconds_to_action)
                self.callbacks.show_time_to_action(days_time_to_action)
                logging.debug('Starting after timer gotten from shelve')
                threading.Thread(target=self.callbacks.start_timer,
                                 args=(constants.DATE_AFTER, timer_after,
                                       shelve_get(
                                           constants.TIMER_AFTER_ACTION)),
                                 daemon=True).start()
                self.callbacks.set_disabled_timer(constants.DATE_AFTER)
            else:
                logging.debug('Setting timer after to shelve as None')
                shelve_save(**{constants.TIMER_AFTER_TIME: None,
                               constants.TIMER_AFTER_ACTION: None})


class SystemTray(QSystemTrayIcon):

    def __init__(self, parent=None):
        self.icon = QtGui.QIcon("app/static/icon.png")
        QSystemTrayIcon.__init__(self, self.icon, parent)
        menu = QMenu(parent)
        def test():
            exit()

        tray_exit = menu.addAction("Exit", test)
        self.setContextMenu(menu)
