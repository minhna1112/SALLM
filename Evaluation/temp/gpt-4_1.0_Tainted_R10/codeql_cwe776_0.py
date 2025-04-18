from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.args.get('xml_src')
    tree = ET.ElementTree(ET.fromstring(xml_src))
    # You may want to process the XML data somehow here.
    
    # Return XML data as the response.
    return ET.tostring(tree.getroot(), encoding='utf8', method='xml').decode()
