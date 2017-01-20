from app import main
import logging
import sys

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.debug('Exit from application')
        sys.exit()
