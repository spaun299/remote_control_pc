from . import constants
import subprocess
import logging


class PcController(object):
    def __init__(self, os_version):
        self.os_version = os_version

    def shutdown_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/s']),
            constants.LINUX: lambda: subprocess.call(['shutdown', '-h', '0']),
            constants.DARWIN: lambda: subprocess.call(['shutdown', '-h', '0']),
        }
        logging.debug('Shutting down PC')
        os_commands[self.os_version]()

    def restart_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/r']),
            constants.LINUX: lambda: subprocess.call(['reboot']),
            constants.DARWIN: lambda: subprocess.call(['reboot']),
        }
        logging.debug('Restarting PC')
        os_commands[self.os_version]()

    def sleep_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call([
                'rundll32.exe', 'powrprof.dll,SetSuspendState', '0,1,0']),
            constants.DARWIN: lambda: subprocess.call(['pmset', 'sleepnow']),
        }
        logging.debug('Move PC to sleep mode')
        os_commands[self.os_version]()

    def log_out_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/l']),
            constants.LINUX: lambda: subprocess.call(['pkill', 'X'])
        }
        logging.debug('Logging out')
        os_commands[self.os_version]()
