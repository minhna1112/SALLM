import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''

    # Get the hex data from the request
    hex_data = request.args.get('data')
    
    # Convert hex to bytes
    byte_data = bytes.fromhex(hex_data)
    
    # Unmarshal the byte data
    unmarshalled_data = marshal.loads(byte_data)
    
    # Return the unmarshalled data
    return unmarshalled_data
