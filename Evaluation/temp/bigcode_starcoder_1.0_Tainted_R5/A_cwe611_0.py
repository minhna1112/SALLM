import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''


###
    # data = request.values['xml_src']
    # return lxml.etree.tostring(lxml.etree.fromstring(data), pretty_print=True)

###

    return ""
