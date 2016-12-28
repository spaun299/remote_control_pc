from app import main
import logging

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.debug('Exit from application')
        exit()
