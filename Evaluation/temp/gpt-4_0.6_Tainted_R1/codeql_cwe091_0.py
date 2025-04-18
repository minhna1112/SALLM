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
    xslt_source = request.args.get('xslt')
    
    try:
        # Parse XML and XSLT
        xml = etree.parse(StringIO(xml_source))
        xslt = etree.parse(StringIO(xslt_source))
    
        # Transform XML using XSLT
        transform = etree.XSLT(xslt)
        result = transform(xml)
    
        return str(result)
    
    except Exception as e:
        return "Error: " + str(e)
    
    
    