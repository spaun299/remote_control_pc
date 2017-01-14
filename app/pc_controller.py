from . import constants
import subprocess
import logging
from .error import BadResponseFromServer


class PcController(object):
    def __init__(self, os_version):
        self.os_version = os_version

    def check_allowed_actions_for_os(self, action):
        allowed_actions = {
            constants.WINDOWS: [constants.SHUTDOWN_TEXT,
                                constants.RESTART_TEXT,
                                constants.SLEEP_TEXT, constants.LOG_OUT_TEXT],
            constants.LINUX: [constants.SHUTDOWN_TEXT, constants.RESTART_TEXT,
                              constants.LOG_OUT_TEXT],
            constants.DARWIN: [constants.SHUTDOWN_TEXT, constants.RESTART_TEXT,
                               constants.SLEEP_TEXT]
        }
        if action not in allowed_actions[self.os_version]:
            raise BadResponseFromServer('Action %s not allowed for this os.\n'
                                        'OS: %s, Allowed actions: %s' % (
                                         action, self.os_version,
                                         ','.join(allowed_actions)))

    def shutdown_pc(self):
        self.check_allowed_actions_for_os(constants.SHUTDOWN_TEXT)
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/s']),
            constants.LINUX: lambda: subprocess.call(['shutdown', '-h', '0']),
            constants.DARWIN: lambda: subprocess.call(['shutdown', '-h', '0']),
        }
        logging.debug('Shutting down PC')
        os_commands[self.os_version]()

    def restart_pc(self):
        self.check_allowed_actions_for_os(constants.RESTART_TEXT)
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/r']),
            constants.LINUX: lambda: subprocess.call(['reboot']),
            constants.DARWIN: lambda: subprocess.call(['reboot']),
        }
        logging.debug('Restarting PC')
        os_commands[self.os_version]()

    def sleep_pc(self):
        self.check_allowed_actions_for_os(constants.SLEEP_TEXT)
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call([
                'rundll32.exe', 'powrprof.dll,SetSuspendState', '0,1,0']),
            constants.DARWIN: lambda: subprocess.call(['pmset', 'sleepnow']),
        }
        logging.debug('Move PC to sleep mode')
        os_commands[self.os_version]()

    def log_out_pc(self):
        self.check_allowed_actions_for_os(constants.LOG_OUT_TEXT)
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/l']),
            constants.LINUX: lambda: subprocess.call(['pkill', 'X'])
        }
        logging.debug('Logging out')
        os_commands[self.os_version]()
