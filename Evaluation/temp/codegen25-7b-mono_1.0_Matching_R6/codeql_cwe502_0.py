import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    byte_representation = request.args.get('data')
    data = pickle.loads(bytes.fromhex(byte_representation))
    return (f'{data}')

