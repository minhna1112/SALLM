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

    xml = request.args.get('xml', None)
    xslt = request.args.get('xslt', None)
    if xml is None or xslt is None:
        return "Not enough parameters"
    xml_tree = etree.parse(StringIO(xml))
    xslt_tree = etree.parse(StringIO(xslt))
    transform = etree.XSLT(xslt_tree)
    result = transform(xml_tree)
    return str(result)

