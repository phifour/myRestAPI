from flask import Flask, jsonify, abort, request
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
#from sklearn import tree

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

@app.route('/test', methods=['GET'])
def getMessage():
    data = {'message': 'Hello Test!'}
    return jsonify(data)

app.run(debug=False)
