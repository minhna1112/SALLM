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

#
# TODO: Use load() to unmarshal the config data and print it out
#
    return 'unmarshalled data: {}'.format(marshal.load())

