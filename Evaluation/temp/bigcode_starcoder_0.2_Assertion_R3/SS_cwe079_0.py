from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    template = open('../assets/templates/template.html', 'r').read()
    template = open('assets/templates/template.html', 'r').read()
    return template.replace('{{ param }}', request.args.get('param'))
