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

#    global gpx
    source = str(request.args['xml'])
    xslt = str(request.args['xslt'])

    xml = etree.fromstring(source)
    transform = etree.parse(xslt)

    result = transform.apply(xml)  # etree.XSLT(transform).apply(xml)

    return etree.tostring(result, pretty_print=True)

