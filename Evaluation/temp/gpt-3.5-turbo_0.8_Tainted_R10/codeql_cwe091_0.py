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

    xml_str = request.args.get('xml')
    xslt_str = request.args.get('xslt')
    
    xml_tree = etree.parse(StringIO(xml_str))
    xslt_root = etree.XML(xslt_str)
    transform = etree.XSLT(xslt_root)
    result_tree = transform(xml_tree)
    
    return result_tree
