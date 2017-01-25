from functools import wraps
import logging
import config
import os
import sys


def is_valid_shelve(folder):
    def func_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except PermissionError:
                logging.debug('Can"t open shelve file. Permission denied.'
                              'Recreating shelve files')
                app_doc_folder = folder
                shelve_dir_file = app_doc_folder + '/%s.dir' % config.shelve_file_name
                shelve_dat_file = app_doc_folder + '/%s.dat' % config.shelve_file_name
                shelve_bak_file = app_doc_folder + '/%s.bak' % config.shelve_file_name
                for f in (shelve_bak_file, shelve_dat_file, shelve_dir_file):
                    os.remove(f)
                with open(shelve_dat_file, 'a'):
                    pass
                with open(shelve_dir_file, 'a'):
                    pass
                try:
                    res = func(*args, **kwargs)
                except Exception as e:
                    logging.error('Something wrong with shelve files.\n'
                                  'Error: %s' % e)
                    sys.exit(1)
            return res
        return wrapper
    return func_decorator
