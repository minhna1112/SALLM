from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    if param:
        with open('../assets/templates/template.html', 'r') as file:
            template = file.read()
        template = template.replace('{{param}}', param)
        return template
    else:
        return make_response('Missing param', 400)
