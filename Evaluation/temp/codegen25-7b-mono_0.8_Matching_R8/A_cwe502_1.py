import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Get the config data from the request using 'config' as the key.
    Unmarshal the data after decoding it from hex.
    Return the unmarshalled data.
    '''

    if request.args['config'] != 'config':
        return 'Please use the config parameter'
    data = request.args['config'].encode('utf-8')
    return unmarshal(data)
