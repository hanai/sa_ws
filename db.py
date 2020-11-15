from flask import current_app, g
from flask.cli import with_appcontext

from ..sa_db import TickerSession, DailyPriceSession


def get_db():
    if 'db' not in g:
        g.db = {"ticker": TickerSession(), "daily_price": DailyPriceSession()}
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        for key, value in db.items():
            value.close()


def init_app(app):
    app.teardown_appcontext(close_db)
