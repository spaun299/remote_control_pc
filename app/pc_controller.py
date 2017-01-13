from . import constants
import subprocess


class PcController(object):
    def __init__(self, os_version):
        self.os_version = os_version

    def shutdown_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/s']),
            constants.LINUX: lambda: subprocess.call(['shutdown', '-h', '0']),
            constants.DARWIN: lambda: subprocess.call(['shutdown', '-h', '0']),
        }
        os_commands[self.os_version]()

    def restart_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/r']),
            constants.LINUX: lambda: subprocess.call(['reboot']),
            constants.DARWIN: lambda: subprocess.call(['reboot']),
        }
        os_commands[self.os_version]()

    def sleep_pc(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call([
                'rundll32.exe', 'powrprof.dll,SetSuspendState', '0,1,0']),
            constants.DARWIN: lambda: subprocess.call(['pmset', 'sleepnow']),
        }
        os_commands[self.os_version]()

    def log_out(self):
        os_commands = {
            constants.WINDOWS: lambda: subprocess.call(['shutdown', '/l']),
            constants.LINUX: lambda: subprocess.call(['pkill', 'X'])
        }
        os_commands[self.os_version]()
