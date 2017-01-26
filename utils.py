import datetime
import time
import shelve
import os
import config
import logging
import webbrowser
from app import constants
import sys
from app.decorators import is_valid_shelve
from PyQt5 import QtGui


def documents_folder():
    return os.path.expanduser('~/Documents')


def get_folder_path_in_documents(folder=config.applicatin_show_name):
    return documents_folder() + '/' + folder


@is_valid_shelve(get_folder_path_in_documents())
def shelve_get(key):
    logging.debug('Getting shelve value for key: %s' % key)
    shelve_file = shelve.open(get_folder_path_in_documents() + '/' +
                              config.shelve_file_name)
    return shelve_file.get(key)


@is_valid_shelve(get_folder_path_in_documents())
def shelve_get_dict():
    logging.debug('Getting all shelve file as dictionary')
    shelve_obj = shelve.open(
        get_folder_path_in_documents() + '/' + config.shelve_file_name)
    return dict(shelve_obj)


@is_valid_shelve(get_folder_path_in_documents())
def shelve_delete(key):
    logging.debug('Delete shelve value for key: %s' % key)
    shelve_file = shelve.open(
        shelve.open(get_folder_path_in_documents() + '/' +
                    config.shelve_file_name),
        writeback=True)
    del shelve_file[key]


@is_valid_shelve(get_folder_path_in_documents())
def shelve_save(**kwargs):
    logging.debug('Saving shelve values: %s' % kwargs)
    shelve_file = shelve.open(
        get_folder_path_in_documents() + '/' + config.shelve_file_name,
        writeback=True)
    for k, v in kwargs.items():
        shelve_file[k] = v


def current_date_time(dt_format='%Y/%m/%d %H:%M'):
    logging.debug('Getting current datetime')
    return datetime.datetime.now().strftime(dt_format)


def current_time(t_format='%M:%S'):
    logging.debug('Getting current time')
    return datetime.datetime.now().strftime(t_format)


def seconds_from_time(str_time):
    logging.debug('Getting seconds from time string: %s' % str_time)
    hours, minutes = str_time.split(':')
    seconds = int(hours) * 3600 + int(minutes) * 60
    return seconds


def seconds_from_datetime(str_date_time, tm_format='%m/%d/%y %H:%M'):
    logging.debug('Getting seconds from datetime string: %s' % str_date_time)
    seconds = time.mktime(datetime.datetime.strptime(
        str_date_time, tm_format).timetuple())
    return seconds


def format_hours_minutes_from_seconds(seconds):
    logging.debug('Getting minutes, hours from SECONDS: %s' % seconds)
    tm_from_sec = str(datetime.timedelta(seconds=seconds))
    result = str(tm_from_sec)
    if '.' in result:
        result = ','.join(result.split('.')[:-1])
    else:
        result = ':'.join(result.split(':'))
    return result


def get_future_date_from_time(hours, minutes, tm_format='%m/%d/%y %H:%M'):
    logging.debug('Getting future datetime from hours, minutes: %s:%s' % (
        hours, minutes))
    date_from = datetime.datetime.now()
    date_future = date_from + datetime.timedelta(hours=int(hours),
                                                 minutes=int(minutes))
    return date_future.strftime(tm_format)


def open_web_page_in_browser(www):
    webbrowser.open(www, new=2)


def get_pc_os():
    # check current operation system
    possible_os = (constants.DARWIN, constants.WINDOWS, constants.LINUX,
                   constants.LINUX2)
    current_os = sys.platform
    if current_os not in possible_os:
        # if current os is not supported, exit from app
        logging.error('%s os is not supported' % current_os)
        raise KeyboardInterrupt
    logging.debug('Current os %s ' % current_os)
    return current_os


def get_font(family="Courier", size=22, weight=75, bold=False):
    font = QtGui.QFont()
    font.setFamily(family)
    font.setPointSize(size)
    font.setBold(bold)
    font.setWeight(weight)
    return font
