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

    config = request.args.get('config')
    if not config:
        return 'No config data provided'
    try:
        config = config.encode('utf-8')
        config = marshal.loads(bytes.fromhex(config))
        return config
    except Exception as e:
        return str(e)
