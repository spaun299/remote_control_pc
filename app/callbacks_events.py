from PyQt5.QtCore import Qt, QTime
import threading
import time
import utils
from app import constants
import logging
from . import pc_controller


class Callback(pc_controller.PcController):
    instance = None

    def __new__(cls, *args, **kwargs):
        # set as singleton
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, window):
        super(Callback, self).__init__(window.os_version)
        self.widget = window
        self.connect()
        self.register_events()
        self.connect_thread_signals()
        self.action_after_timer = 0
        self.action_at_timer = 0
        self.action_after_timer_do = None
        self.action_at_timer_do = None
        self.cancel_after_timer = False
        self.cancel_at_timer = False
        self.thread_lock = threading.Lock()

    def connect(self):
        """ Connect widgets with callbacks. """
        self.widget.action_after_submit.clicked.connect(
            self.on_click_after_submit)
        self.widget.action_at_submit.clicked.connect(
            self.on_click_at_submit)
        self.widget.action_contribute.triggered.connect(
            self.on_click_contribute)
        self.widget.action_faq.triggered.connect(
            self.on_click_faq)
        self.widget.action_website.triggered.connect(
            self.on_click_website)
        self.widget.action_license.triggered.connect(
            self.on_click_license)
        self.widget.action_contact_us.triggered.connect(
            self.on_click_contact_us)
        self.widget.action_show_all_pc.triggered.connect(
            self.on_click_show_all_pc)
        self.widget.action_sign_out.triggered.connect(
            self.on_click_sign_out)
        self.widget.installUpdates.accepted.connect(
            lambda: self.on_click_install_updates(accepted=True))
        self.widget.installUpdates.rejected.connect(
            lambda: self.on_click_install_updates(accepted=False))
        self.widget.action_after_cancel.clicked.connect(
            lambda: self.on_click_cancel_timer(event=constants.DATE_AFTER)
        )
        self.widget.action_at_cancel.clicked.connect(
            lambda: self.on_click_cancel_timer(event=constants.DATE_AT)
        )
        logging.debug('started')

    def connect_thread_signals(self):
        logging.debug('Connecting thread signals')
        self.widget.notification_signal.connect(
            self.widget.label_notification.setText)
        self.widget.timer_after_signal.connect(
            self.widget.action_after_time.setTime)

    def register_events(self):
        self.widget.closeEvent = self.on_close_event
        self.widget.keyPressEvent = self.on_press_key_event

    def start_timer(self, event, when, action):
        logging.debug('Starting %s timer.\n'
                      'Timeout date time: %s.\n'
                      'Action: %s' % (event, when, action))
        canceled = False
        time_started = int(time.time())
        if event == constants.DATE_AFTER:
            print(when)
            seconds_to_action = utils.seconds_from_datetime(
                when, tm_format='%m/%d/%y %H:%M %S') - time_started
            self.action_after_timer = seconds_to_action
            self.action_after_timer_do = action
            utils.shelve_save(
                **{constants.TIMER_AFTER_TIME: when,
                   constants.TIMER_AFTER_ACTION: action})
            while self.action_after_timer > 0:
                if not self.cancel_after_timer:
                    time.sleep(1)
                    try:
                        self.thread_lock.acquire()
                        self.action_after_timer -= 1
                        days_time_to_action = utils.\
                            format_hours_minutes_from_seconds(
                              self.action_after_timer)
                        if not self.action_at_timer or (
                                    self.action_at_timer >
                                    self.action_after_timer):
                            self.widget.notification_signal.emit(
                                    constants.LABEL_NOTIFICATION_TEXT[action] %
                                    days_time_to_action)
                            if not self.action_after_timer % 60:
                                self.show_time_to_action(days_time_to_action)

                    finally:
                        self.thread_lock.release()
                else:
                    canceled = True
                    self.set_disabled_timer(constants.DATE_AFTER, False)
                    break

        elif event == constants.DATE_AT:
            seconds_to_action = utils.seconds_from_datetime(
                when) - time_started
            self.action_at_timer = seconds_to_action
            self.action_at_timer_do = action
            utils.shelve_save(
                **{constants.TIMER_AT_DATETIME: when,
                   constants.TIMER_AT_ACTION: action})
            while self.action_at_timer > 0:
                if not self.cancel_at_timer:
                    time.sleep(1)
                    try:
                        self.thread_lock.acquire()
                        self.action_at_timer -= 1
                        days_time_to_action = utils.\
                            format_hours_minutes_from_seconds(
                              self.action_at_timer)
                        if not self.action_after_timer or (
                                    self.action_after_timer >
                                    self.action_at_timer):
                            self.widget.notification_signal.emit(
                                constants.LABEL_NOTIFICATION_TEXT[action] %
                                days_time_to_action)
                    finally:
                        self.thread_lock.release()
                else:
                    canceled = True
                    self.set_disabled_timer(constants.DATE_AT, False)
                    break
        self.clear_timer(event)
        if not canceled:
            self.action_ontimer_timeout(event, action)

    def set_disabled_timer(self, event, disabled=True):
        if event == constants.DATE_AT:
            self.widget.action_at_submit.setDisabled(disabled)
            self.widget.action_at_select.setDisabled(disabled)
            self.widget.action_at_datetime.setDisabled(disabled)
        elif event == constants.DATE_AFTER:
            self.widget.action_after_submit.setDisabled(disabled)
            self.widget.action_after_select.setDisabled(disabled)
            self.widget.action_after_time.setDisabled(disabled)

    def show_time_to_action(self, days_time_to_action):
        print(days_time_to_action)
        hrs, mins = [int(val) for val in
                     days_time_to_action.split(
                         ':')[:-1][-2:]]
        self.widget.timer_after_signal.emit(QTime(
            hrs, mins))

    def on_click_cancel_timer(self, event):
        if event == constants.DATE_AFTER:
            self.cancel_after_timer = True
        elif event == constants.DATE_AT:
            self.cancel_at_timer = True

    def clear_timer(self, event, notification_text=''):
        self.widget.notification_signal.emit(notification_text)
        if event == constants.DATE_AFTER:
            self.cancel_after_timer = False
            self.action_after_timer = 0
            self.action_after_timer_do = None
            utils.shelve_save(**{constants.TIMER_AFTER_TIME: None,
                                 constants.TIMER_AFTER_ACTION: None})
        elif event == constants.DATE_AT:
            self.cancel_at_timer = False
            self.action_at_timer = 0
            self.action_at_timer_do = None
            utils.shelve_save(**{constants.TIMER_AT_DATETIME: None,
                                 constants.TIMER_AT_ACTION: None})

    def on_click_after_submit(self):
        print(self.widget.sender().text())
        print(self.widget.action_after_time.text())
        print(self.widget.action_after_select.currentText())
        self.set_disabled_timer(constants.DATE_AFTER)
        hours, minutes = self.widget.action_after_time.text().split(':')
        print(minutes)
        threading.Thread(target=self.start_timer,
                         args=(constants.DATE_AFTER,
                               utils.get_future_date_from_time(
                                   hours, minutes,
                                   tm_format='%m/%d/%y %H:%M %S'),
                               self.widget.action_after_select.currentText()),
                         daemon=True).start()

    def on_click_at_submit(self):
        print(self.widget.sender().text())
        print(self.widget.action_at_datetime.text())
        print(self.widget.action_at_select.currentText())
        self.set_disabled_timer(constants.DATE_AT)
        threading.Thread(target=self.start_timer,
                         args=(constants.DATE_AT,
                               self.widget.action_at_datetime.text(),
                               self.widget.action_at_select.currentText()),
                         daemon=True).start()

    def on_click_contribute(self):
        print(self.widget.action_contribute.text())

    def on_click_faq(self):
        print(self.widget.action_faq.text())

    def on_click_website(self):
        print(self.widget.action_website.text())

    def on_click_license(self):
        print(self.widget.action_license.text())

    def on_click_contact_us(self):
        print(self.widget.action_contact_us.text())

    def on_click_show_all_pc(self):
        print(self.widget.action_show_all_pc.text())

    def on_click_sign_out(self):
        print(self.widget.action_sign_out.text())

    def on_click_install_updates(self, accepted):
        print('Updates accepted' if accepted else 'Updates rejected')

    def on_close_event(self, event):
        self.widget.hide()
        event.ignore()

    def on_press_key_event(self, event):
        if event.key() == Qt.Key_Escape:
            self.widget.hide()

    def action_ontimer_timeout(self, event, action):
        print(action)
        print('what are fuck')
        if event == constants.DATE_AFTER:
            self.set_disabled_timer(constants.DATE_AFTER, False)
        elif event == constants.DATE_AT:
            self.set_disabled_timer(constants.DATE_AT, False)
        self.clear_timer(event, notification_text=constants.
                         PC_ACTION_IN_PROGRESS_TEXT[action])
        possible_actions = {
            constants.SHUTDOWN_TEXT: self.shutdown_pc,
            constants.LOG_OUT_TEXT: self.log_out_pc,
            constants.RESTART_TEXT: self.restart_pc,
            constants.SLEEP_TEXT: self.sleep_pc
        }
        logging.debug('%s PC' % action)
        possible_actions[action]()
