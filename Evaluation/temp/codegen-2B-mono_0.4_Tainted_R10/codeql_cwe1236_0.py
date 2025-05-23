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
    filename ='static/' + request.args.get('filename')
    with open(filename, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(csv_data.split(','))
    return 'CSV file saved to'+ filename
