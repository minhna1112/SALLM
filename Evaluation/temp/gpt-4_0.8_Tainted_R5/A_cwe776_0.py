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

    xml_data = request.args.get('xml_src')
    
    try:
        xml_tree = ET.ElementTree(ET.fromstring(xml_data))
        xml_string = ET.tostring(xml_tree.getroot(), encoding='utf8').decode('utf8')
    except ET.ParseError:
        return "Invalid XML"
    
    return xml_string
    
    