from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.data
    tree = lxml.etree.fromstring(xml_src)
    
    return lxml.etree.tostring(tree, pretty_print=True).decode()
    
    