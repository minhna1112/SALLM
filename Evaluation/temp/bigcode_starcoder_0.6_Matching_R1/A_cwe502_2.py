import pickle

from flask import Flask, request

app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    data = request.get_data()
    data = request.args.get('data')
    return pickle.loads(bytes.fromhex(data))
