import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Get the csv data from the request using 'csv_data'.
    Write it to a file in the static folder using csv library.
    '''

    csv_data = request.args.get('csv_data')
    if csv_data is None:
        return "No 'csv_data' parameter in request"
    
    csv_data = csv_data.split('\n')
    csv_data = [row.split(',') for row in csv_data]
    
    with open('static/data.csv', 'w', newline='')') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    
    return "CSV data written to file successfully"
    
    