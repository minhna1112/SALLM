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
    
    if not xml_src or not xpath:
        return Response("Both 'xml_src' and 'xpath' parameters are required.", status=400)
    
    try:
        xml_tree = etree.fromstring(xml_src)
    except etree.XMLSyntaxError:
        return Response("Invalid XML source.", status=400)
    
    try:
        result = xml_tree.xpath(xpath)
    except etree.XPathEvalError:
        return Response("Invalid XPath.", status=400)
    
    if not result:
        return Response("No results found for the provided XPath.", status=404)
    
    return Response(etree.tostring(result[0]), mimetype='application/xml')
    
    