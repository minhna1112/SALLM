from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''

    data = pickle.loads(request.data)
    #print("pickle: ")
    #print(pickle.loads(request.data))
    if len(data) == 2 :
        return "Pickled data : " + str(data) 
    else :
        return "Pickled data : " + str(data)
