import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/unpickled_data')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

#    data = request.get_json()
#    pickled = data['data']
    pickled = request.args.get('data')
    pickled = bytes.fromhex(pickled)
    data = pickle.loads(pickled)
    return str(data)

