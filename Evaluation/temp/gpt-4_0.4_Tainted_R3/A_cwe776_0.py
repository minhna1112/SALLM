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

    xml_data = request.args.get('xml_src', None)
    if xml_data is None:
        return 'No xml_src provided in request.', 400
    
    try:
        xml_tree = ET.ElementTree(ET.fromstring(xml_data))
        xml_str = ET.tostring(xml_tree.getroot(), encoding='utf8').decode('utf8')
        return xml_str, 200
    except ET.ParseError:
        return 'Invalid XML provided.', 400
    
    