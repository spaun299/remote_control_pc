from PyQt5.QtWidgets import QApplication
from app.main_window import MainWindow
import os
import sys
from utils import documents_folder, get_folder_path_in_documents, \
    shelve_get_dict, shelve_save
from config import shelve_file_name
from app import constants


def main():
    app = QApplication(sys.argv)
    check_and_create_necessarry_files_and_folders()
    shelve_necessarry_fields()
    form = MainWindow()
    form.show()
    app.exec_()


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
    shelve_dict = shelve_get_dict()
    for field in fields:
        if field not in shelve_dict:
            shelve_save(field=None)
