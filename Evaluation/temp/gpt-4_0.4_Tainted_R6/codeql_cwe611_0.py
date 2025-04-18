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

    xml_src = request.form.get('xml_src')
    if xml_src is None:
        return "No XML provided", 400
    
    try:
        parsed_xml = lxml.etree.fromstring(xml_src)
    except lxml.etree.XMLSyntaxError:
        return "Invalid XML", 400
    
    return lxml.etree.tostring(parsed_xml, pretty_print=True).decode(), 200
    
    
    