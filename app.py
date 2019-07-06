from flask import flask, request

from secrets import URL


app = Flask(__name__)

@app.route(URL)
def wake():
    pass
