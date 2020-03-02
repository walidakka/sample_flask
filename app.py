from flask import Flask, request
from functions import percentage_function

app = Flask(__name__)


@app.route('/')
def hello():
    return {'hello': 'Walid'}


@app.route('/percentage', methods=['POST'])
def calculate_percentage():
    req = request.get_json()
    return {'Result': percentage_function(req['a'], req['b'])}


app.run()
