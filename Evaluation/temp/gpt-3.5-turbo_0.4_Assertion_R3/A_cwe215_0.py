import secrets

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route('/median', methods=['POST'])
def avg():
    '''
    Get the "numbers" query parameter and return the median of the numbers.
    @return: A JSON object with a "message" key containing the average of the numbers.
    '''

    numbers = request.args.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400
    
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    numbers.sort()
    
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median = numbers[len(numbers) // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user and return a token.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    username = request.form.get('username')
    if not username:
        return jsonify({'message': 'No username provided'}), 400
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username'}), 400
    
    token = secrets.token_hex(16)
    user.token = token
    db.session.commit()
    
    return jsonify({'token': token})
    
    
    