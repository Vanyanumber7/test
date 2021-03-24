import os

from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # app.run(port=port, host="0.0.0.0")

    # с дефаултными значениями будет не более 4 потов
    serve(app, port=port, host="0.0.0.0")
