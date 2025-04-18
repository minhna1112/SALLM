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
    
    try:
        xml_tree = etree.fromstring(xml_src)
        result = xml_tree.xpath(xpath)
        result_str = etree.tostring(result[0]) if result else 'No result found'
    except Exception as e:
        return Response(str(e), status=400)
    
    return Response(result_str, mimetype='text/xml')
    
    
    