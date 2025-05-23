from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = float(request.args.get('total_score', 0))
    total_count = float(request.args.get('total_count', 0))
    
    if total_count == 0:
        return Response("Total count can't be zero", status=400)
    
    average_score = total_score / total_count
    return Response(str(average_score), mimetype='text/plain')
    
    
    