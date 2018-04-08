# -*- coding: utf-8 -*-

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

from contextlib import closing

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

from mold.mold import tree_mold
from torrent.torrent import bp_torrent

app.register_blueprint(tree_mold, url_prefix="/oak")
app.register_blueprint(tree_mold, url_prefix="/fir")
app.register_blueprint(tree_mold, url_prefix="/ash")

app.register_blueprint(bp_torrent, url_prefix="/torrent")

if __name__ == '__main__':
    app.run()
