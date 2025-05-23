import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    data = request.args.get("data")
    logging.info(f"Received data: {data}")
    return {"data": data}, 200
    
    