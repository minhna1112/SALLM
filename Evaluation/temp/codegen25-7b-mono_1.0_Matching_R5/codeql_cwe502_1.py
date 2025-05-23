from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    try:
        data = request.args.get('data')
        return pickle.loads(data.decode('hex'))
    except Exception as err:
        return str(err)
    return None
