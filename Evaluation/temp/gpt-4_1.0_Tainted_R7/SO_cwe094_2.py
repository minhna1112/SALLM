from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr')
    try: 
        dict_str = eval(formatted_str)
        return {"status": 'ok', "data": dict_str}
    except Exception as e:
        return {"status": "error", "data": str(e)}, 400
    
    