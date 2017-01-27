from PyQt5.QtWidgets import QMainWindow
from .callbacks_events import Callback
from PyQt5.QtCore import pyqtSignal, QTime
from PyQt5.QtGui import QIcon
import config
import datetime
from utils import shelve_get, seconds_from_datetime, shelve_save, \
    format_hours_minutes_from_seconds, open_web_page_in_browser, get_pc_os, \
    get_font
from app import constants
import threading
import time
import logging
from .system_tray import SystemTray
from .http_server.run import run as run_http_server
from urllib.request import urlopen, URLError
os_version = get_pc_os()
if os_version == constants.DARWIN:
    from .base_ui_osx import Ui_MainWindow
elif os_version == constants.WINDOWS:
    from .base_ui_windows import Ui_MainWindow
elif os_version in (constants.LINUX, constants.LINUX2):
    from .base_ui_linux import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    notification_signal = pyqtSignal(str, name=constants.NOTIFICATION)
    timer_after_signal = pyqtSignal(QTime, name=constants.TIMER_AFTER)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.os_version = os_version
        self.run_from_dt = datetime.datetime.now()
        self.run_from_timestamp = time.time()
        self.setup_app()
        self.callbacks = Callback(self)
        self.tray_icon = SystemTray(self)
        self.tray_icon.show()
        threading.Thread(target=run_http_server, daemon=True,
                         args=(self, )).start()
        self._app_status = None
        self.app_status = None

    @property
    def app_status(self):
        return self._app_status or constants.STATUS_UP_TO_DATE

    @app_status.setter
    def app_status(self, val):
        logging.debug('Changing application status to %s' % val)
        # if old status(before this one) was NEED_UPDATE,
        # we should to erase notification text about updates
        if self._app_status == constants.STATUS_NEED_UPDATE:
            self.hide_install_updates()
        if val is None:
            if not self.check_internet_connection():
                val = constants.STATUS_NO_INTERNET
            elif self.check_for_new_updates():
                val = constants.STATUS_NEED_UPDATE
            else:
                val = constants.STATUS_UP_TO_DATE
        if val == constants.STATUS_UP_TO_DATE:
            font = get_font(bold=True)
            self.change_background_color(constants.background_color_green)
            self.upper_widget_label.setFont(font)
        elif val == constants.STATUS_NO_INTERNET:
            font = get_font(size=18, weight=65, bold=True)
            self.change_background_color(constants.background_color_red)
            self.upper_widget_label.setFont(font)
        elif val == constants.STATUS_NEED_UPDATE:
            font = get_font(size=16, weight=62, bold=True)
            self.change_background_color(constants.background_color_yellow)
            self.upper_widget_label.setFont(font)
            self.bottom_widget_label.setText(
                constants.LABEL_NOTIFICATION_TEXT['new_updates_available'])
            self.installUpdates.show()
        self._app_status = val
        status_text = constants.STATUS_TEXT[val]
        self.tray_icon.show_notification.setText(status_text)
        self.upper_widget_label.setText(status_text)

    def check_for_new_updates(self):
        # TODO: MUST BE IMPLEMENTED
        logging.debug('Checking for new updates')
        return False

    @staticmethod
    def check_internet_connection():
        """ check if there is internet connection.
            :return True if OK, and False if no IC """
        logging.debug('Checking internet connection')
        try:
            urlopen(config.api_base_url,
                    timeout=config.timeout_internet_connection)
            logging.debug('Connected to the internet')
            return True
        except URLError as err:
            logging.debug('No internet connection')
            return False

    def change_background_color(self, color):
        self.background_widget.setStyleSheet(
            "QWidget #background_widget{background-color: %s}" % color)

    def hide_install_updates(self):
        self.bottom_widget_label.setText("")
        self.installUpdates.hide()

    def setup_app(self):
        logging.debug('Setting up UI application...')
        self.setupUi(self)
        self.setWindowIcon(QIcon(config.app_icon_path))
        self.hide_install_updates()
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
        self.action_at_datetime.setDisplayFormat('MM/dd/yy hh:mm')
        if self.os_version == constants.DARWIN:
            self.action_after_select.removeItem(2)
            self.action_at_select.removeItem(2)
        elif self.os_version in (constants.LINUX, constants.LINUX2):
            self.action_at_select.removeItem(3)
            self.action_after_select.removeItem(3)
        logging.debug('Getting values from shelve for timers')
        timer_at = shelve_get(constants.TIMER_AT_DATETIME)
        timer_after = shelve_get(constants.TIMER_AFTER_TIME)
        self.callbacks = Callback(self)
        if timer_at:
            logging.debug('At timer exists in shelve file. \n'
                          'Timer at time: %s' % timer_at)
            if seconds_from_datetime(timer_at) > self.run_from_timestamp:
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
                    timer_after, tm_format='%m/%d/%y %H:%M %S') - \
                                    self.run_from_timestamp
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

    def show_notification_label(self, text):
        logging.debug('Show notification label. \nText: ' % text)
        self.label_notification.setText(text)

    def open_web_site(self):
        open_web_page_in_browser(config.web_site)
