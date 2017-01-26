DATE_AT = 'at'
DATE_AFTER = 'after'
USER_NAME = 'user_name'
USER_PASSWORD = 'user_password'
TIMER_AFTER_TIME = 'timer_after_time'
TIMER_AT_DATETIME = 'timer_at_datetime'
TIMER_AFTER_ACTION = 'timer_after_action'
TIMER_AT_ACTION = 'timer_at_action'
APP_VERSION = 'app_version'
TIMER_AFTER = 'timer_after'
NOTIFICATION = 'notification'
NOTIFICATION_TRAY = 'notification_tray'
NOW = 'now'
STATUS_UP_TO_DATE = 'up_to_date'
STATUS_NEED_UPDATE = 'need_update'
STATUS_NO_INTERNET = 'no_internet_connection'
# ---------------
# possible actions with pc
SHUTDOWN_TEXT = 'Shutdown'
RESTART_TEXT = 'Restart'
SLEEP_TEXT = 'Sleep'
LOG_OUT_TEXT = 'LogOut'
HIBERNATE_TEXT = 'Hibernate'
# texts which will appear when some action is processing
PC_ACTION_IN_PROGRESS_TEXT = {
    SHUTDOWN_TEXT: 'Shutting down pc...',
    RESTART_TEXT: 'Restarting pc...',
    SLEEP_TEXT: 'Moving PC to sleep mode...',
    LOG_OUT_TEXT: 'Logging out...',
    HIBERNATE_TEXT: 'Moving PC to hibernate mode...'}
# ---------------
# notification texts
LABEL_NOTIFICATION_TEXT = {
    RESTART_TEXT: "Your computer will be restarted in %s",
    SHUTDOWN_TEXT: "Shutting down computer in %s",
    SLEEP_TEXT: "Your computer will be in sleep mode in %s",
    LOG_OUT_TEXT: "Logging out in %s",
    HIBERNATE_TEXT: "Your computer will be in hibernate mode in %s",
    'time_less_zero': "Incorrect date. Please enter a future date",
    'new_updates_available': 'There are new updates.Install?'}
# ---------------
# statuses text
STATUS_TEXT = {
    STATUS_UP_TO_DATE: "Program is Running...",
    STATUS_NEED_UPDATE: "Please install new updates!",
    STATUS_NO_INTERNET: "No Internet connection!"
}
# ---------------
# constants for client api
NOW_INT = 0
SHUTDOWN = 1
RESTART = 2
SLEEP = 3
HIBERNATE = 4
SERVER_ERROR = 5
LOG_OUT = 6
# ---------------
# computer possible os
DARWIN = 'darwin'
WINDOWS = 'win32'
LINUX = 'linux'
LINUX2 = 'linux2'
# ---------------
# everything associated with UI part
background_color_green = "qlineargradient(spread:pad, x1:0.502, y1:0," \
                         " x2:0.507, y2:1, stop:0.444976 " \
                         "rgba(27, 188, 155, 255), stop:1 " \
                         "rgba(255, 255, 255, 255))"
background_color_yellow = "qlineargradient(spread:pad, x1:0.502, y1:0," \
                          " x2:0.507, y2:1, stop:0.444976 " \
                          "rgba(245, 171, 53, 1), stop:1 " \
                          "rgba(255, 255, 255, 255))"
background_color_red = "qlineargradient(spread:pad, x1:0.502, y1:0," \
                       " x2:0.507, y2:1, stop:0.444976 " \
                       "rgba(242, 38, 19, 1), stop:1 " \
                       "rgba(255, 255, 255, 255))"
