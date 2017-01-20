from flask import Flask, g
import socket
import logging
from config import debug

app = Flask(__name__)


def before_request(qt_app):
    g.qt_app = qt_app


def run(qt_app):
    app.before_request(lambda: before_request(qt_app))
    if debug:
        port = 5222
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        port = sock.getsockname()[1]
        sock.close()
    try:
        logging.debug('Starting flask app at port %s ' % port)
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        logging.error("Can't start flask server. \nError: %s" % e)

from .api import *
