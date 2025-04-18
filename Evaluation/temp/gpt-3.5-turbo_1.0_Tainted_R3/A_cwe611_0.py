import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    # Retrieve the XML source from the request
    xml_src = request.args.get('xml_src')
    
    # Parse the XML from the string
    root = lxml.etree.fromstring(xml_src)
    
    # Return the XML as a string
    return lxml.etree.tostring(root)
