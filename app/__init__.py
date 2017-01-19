from PyQt5.QtWidgets import QApplication
from app.main_window import MainWindow
import os
import sys
from utils import documents_folder, get_folder_path_in_documents, \
    shelve_get_dict, shelve_save
from config import shelve_file_name, debug, log_name, logger_backup_count, \
    logger_max_bytes
from app import constants
import logging
import logging.handlers


def main():
    configure_logging()
    logging.debug('Starting application...')
    app = QApplication(sys.argv)
    check_and_create_necessarry_files_and_folders()
    shelve_necessarry_fields()
    os_version = get_pc_os()
    form = MainWindow(os_version)
    form.show()
    app.exec_()


def configure_logging():
    """ configure logger for application """
    try:
        logging.basicConfig(
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y/%m/%d %H:%M:%S',
                            level=logging.DEBUG if debug else logging.ERROR,
                            handlers=[logging.handlers.RotatingFileHandler(
                                filename='%s/%s' % (
                                    get_folder_path_in_documents(),
                                    log_name),
                                maxBytes=logger_max_bytes,
                                backupCount=logger_backup_count
                            )])
    except FileNotFoundError:
        check_and_create_necessarry_files_and_folders()


def check_and_create_necessarry_files_and_folders():
    doc_folder = documents_folder()
    app_doc_folder = get_folder_path_in_documents()
    shelve_dir_file = app_doc_folder + '/%s.dir' % shelve_file_name
    shelve_dat_file = app_doc_folder + '/%s.dat' % shelve_file_name
    if not os.path.exists(doc_folder):
        os.makedirs(doc_folder)
    if not os.path.exists(app_doc_folder):
        os.makedirs(app_doc_folder)
    with open(shelve_dat_file, 'a'):
        pass
    with open(shelve_dir_file, 'a'):
        pass


def shelve_necessarry_fields():
    fields = [constants.APP_VERSION, constants.DATE_AFTER,
              constants.DATE_AT, constants.TIMER_AFTER_ACTION,
              constants.TIMER_AFTER_TIME, constants.TIMER_AT_ACTION,
              constants.TIMER_AT_DATETIME, constants.USER_NAME,
              constants.USER_PASSWORD]
    logging.debug('Checking necessary shelve fields.\n'
                  'Necessary fields: %s', ','.join(fields))
    shelve_dict = shelve_get_dict()
    for field in fields:
        if field not in shelve_dict:
            logging.debug('Shelve field %s not exists. Set as None' % field)
            shelve_save(**{field: None})


def get_pc_os():
    # check current operation system
    possible_os = (constants.DARWIN, constants.WINDOWS, constants.LINUX, constants.LINUX2)
    current_os = sys.platform
    if current_os not in possible_os:
        # if current os is not supported, exit from app
        logging.error('%s os is not supported' % current_os)
        raise KeyboardInterrupt
    logging.debug('Current os %s ' % current_os)
    return current_os
