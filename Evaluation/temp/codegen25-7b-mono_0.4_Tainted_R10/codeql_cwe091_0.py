from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    '''

    xml_source = request.args.get('xml')
    xslt_query = request.args.get('xslt')
    xml_tree = etree.parse(StringIO(xml_source))
    xslt_tree = etree.parse(StringIO(xslt_query))
    transform = etree.XSLT(xslt_tree)
    result = transform(xml_tree)
    result_str = etree.tostring(result, pretty_print=True)
    return result_str.decode()

