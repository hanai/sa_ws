from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    from . import db
    db.init_app(app)

    CORS(app)

    return app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello, World!'


from . import routes
