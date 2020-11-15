from .. import app
from flask import request, jsonify
from datetime import datetime

from ...sa_db import (DailyPriceSession, get_daily_price_model)

from ..db import get_db


@app.route('/daily_price/<symbol>', methods=['GET'])
def get_daily_price(symbol):
    start_date = datetime.strptime(request.args.get('start_date'), '%Y%m%d')
    end_date = datetime.strptime(request.args.get('end_date'), '%Y%m%d')

    Model = get_daily_price_model(symbol)

    session = get_db()['daily_price']
    res = session.query(Model).filter(Model.date >= start_date,
                                      Model.date <= end_date).all()
    res = [x._asdict() for x in res]
    for i in res:
        i['date'] = i['date'].strftime('%Y-%m-%d')
    return jsonify(res)
