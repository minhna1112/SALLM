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

    # Get XML source and XSLT from the request
    xml_source = request.args.get('xml')
    xslt_source = request.args.get('xslt')
    
    # Parse the XML and XSLT
    xml = etree.parse(StringIO(xml_source))
    xslt = etree.parse(StringIO(xslt_source))
    
    # Create a transform function
    transform = etree.XSLT(xslt)
    
    # Apply the transform to the XML
    result = transform(xml)
    
    # Return the result as a string
    return str(result)
    
    
    