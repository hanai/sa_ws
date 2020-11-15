from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import db
    db.init_app(app)

    return app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello, World!'


from . import routes
