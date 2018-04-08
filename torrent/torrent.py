# An example
from flask import Blueprint
import threading
import time
from .torrentkim import Torrentkim

bp_torrent = Blueprint("torrent", __name__)


@bp_torrent.route('/')
def root():
    return 'I will show you list of them'


@bp_torrent.route('/rss')
def rss():
    return 'This is my RSSs of torrent, that I collected from many torrent sites'


collect_threading = None


@bp_torrent.route('/collect')
def collect():
    Torrentkim.collect()

    global collect_threading

    if collect_threading and collect_threading.isAlive():
        msg = "site 요청이 처리중입니다."
    else:
        collect_threading = threading.Thread(target=collect_backgound, args=(), kwargs={})
        collect_threading.setDaemon(True)
        collect_threading.start()
        msg = "site 요청되었습니다."

    return 'collect sth' + msg


def collect_backgound():
    sec = 3.14
    time.sleep(sec)
    print('run in background')
