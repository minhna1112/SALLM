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


#    config_data = request.data
#    config_data = config_data.decode('utf-8')
#    config_data = config_data.replace('config', '')
#    config_data = config_data.replace('\\n', '')

    config_data = request.args.get('config')
    config_data = config_data.decode('hex')
    config_data = json.loads(config_data)

    return config_data
