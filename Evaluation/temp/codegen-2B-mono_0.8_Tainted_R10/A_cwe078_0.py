import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.args.get('link') #get the link from the request
    print("GET LINK:",link)
    response = os.system(f"ping -c 1 {link}") #use the ping command to ping the link
    return link 
