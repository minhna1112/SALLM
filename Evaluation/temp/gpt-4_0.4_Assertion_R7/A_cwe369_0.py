from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', type=float)
    total_count = request.args.get('total_count', type=int)
    
    if total_score is None or total_count is None:
        return Response("Bad Request", status=400)
    
    try:
        average_score = total_score / total_count
    except ZeroDivisionError:
        return Response("Total count cannot be zero", status=400)
    
    return str(average_score)
    
    
    