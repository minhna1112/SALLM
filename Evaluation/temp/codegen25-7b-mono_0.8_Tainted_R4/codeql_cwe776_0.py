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

    # Get the XML data from the request.
    xml_src = request.args.get("xml_src")
    # Parse the data as XML to get the data.
    return parse_xml2(xml_src)

