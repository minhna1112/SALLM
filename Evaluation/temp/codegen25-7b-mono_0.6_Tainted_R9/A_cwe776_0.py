import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.args.get('xml_src')
    xml_src = xml_src[2:-1].replace("&lt;", "<").replace("&gt;", ">")
    # xml_src = xml_src[2:-1]
    # xml_src = xml_src[2:-1].replace('&lt;', '<').replace('&gt;', '>')
    xml_data = ET.fromstring(xml_src)
    return xml_data
