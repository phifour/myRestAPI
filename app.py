from loan import *

from flask import Flask
app = Flask(__name__)

@app.route("/loan/<f>/<n>/<r>")
def loan(f,n,r):
    return calc_cashflows(f,n,r)
