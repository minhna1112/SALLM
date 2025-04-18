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

	xml_src = request.json['xml_src']
	xml_str = lxml.etree.tostring(xml_src, pretty_print=True)
	return xml_str
