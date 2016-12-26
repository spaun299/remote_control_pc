from .base_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from .callbacks_events import Callback
from PyQt5.QtCore import Qt, pyqtSignal, QDateTime, QTime, QTimer
import config
import datetime
from utils import shelve_get, seconds_from_datetime, shelve_save
from app import constants
import threading
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    notification_signal = pyqtSignal(str, name=constants.NOTIFICATION)
    timer_after_signal = pyqtSignal(QTime, name=constants.TIMER_AFTER)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.run_from_dt = datetime.datetime.now()
        self.setup_app()
        self.callbacks = Callback(self)
        self.on_run_app()

    def setup_app(self):
        self.setupUi(self)
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
        self.label_notification.setText(text)

    def on_run_app(self):
        timer_at = shelve_get(constants.TIMER_AT_DATETIME)
        timer_after = shelve_get(constants.TIMER_AFTER_TIME)
        if timer_at:
            print(timer_at)
            if seconds_from_datetime(timer_at) > time.time():
                self.callbacks.show_time_to_action(timer_at)
                threading.Thread(target=self.callbacks.start_timer,
                                 args=(constants.DATE_AT, timer_at,
                                       shelve_get(constants.TIMER_AT_ACTION))
                                 ).start()
                self.callbacks.set_disabled_timer(constants.DATE_AT)

            else:
                shelve_save(**{constants.TIMER_AT_DATETIME: None,
                               constants.TIMER_AT_ACTION: None})
        if timer_after:
            if seconds_from_datetime(timer_after,
                                     tm_format='%m/%d/%y %H:%M %S') > \
                    time.time():
                threading.Thread(target=self.callbacks.start_timer,
                                 args=(constants.DATE_AFTER, timer_after,
                                       shelve_get(
                                           constants.TIMER_AFTER_ACTION))
                                 ).start()
                self.callbacks.set_disabled_timer(constants.DATE_AFTER)
            else:
                shelve_save(**{constants.TIMER_AFTER_TIME: None,
                               constants.TIMER_AFTER_ACTION: None})
