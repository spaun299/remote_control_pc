import logging


class BadResponseFromServer:
    def __init__(self, msg):
        self.msg = msg
        logging.error(msg)
        logging.debug(msg)

    def __repr__(self):
        return 'Error while reading response. Message:\n%s' % self.msg
