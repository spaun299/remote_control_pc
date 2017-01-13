from .run import app
from flask import g


@app.route('/ping')
def ping():
    g.qt_app.notification_signal.emit('It Works')
    return 'Hello'
