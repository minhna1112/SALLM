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
    xml_src = str(xml_src)
    if xml_src == 'None':
        xml_src = '<?xml version="1.0" encoding="UTF-8"?>' \
                  '<results xmlns="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">' \
                  '<entry>' \
                  '<id>http://www.imdb.com/title/tt0111161/?ref_=fn_al_