from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''

    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    
    # Parse the XML
    xml_tree = etree.fromstring(xml_src)
    
    # Query the XML using the xpath
    result = xml_tree.xpath(xpath)
    
    # Convert the result to string
    result_str = etree.tostring(result[0], pretty_print=True).decode()
    
    return Response(result_str, mimetype='text/xml')
