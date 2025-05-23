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

    # Check if the request is authorized
    token = request.headers.get('Authorization')
    user = User.query.filter_by(token=token).first()
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Check if the "numbers" parameter is present
    numbers = request.json.get('numbers')
    if numbers is None:
        return jsonify({'message': 'Missing "numbers" parameter'}), 400
    
    # Check if "numbers" is a list
    if not isinstance(numbers, list):
        return jsonify({'message': '"numbers" parameter should be a list'}), 400
    
    # Check if "numbers" is not empty
    if len(numbers) == 0:
        return jsonify({'message': '"numbers" parameter should not be empty'}), 400
    
    # Check if all elements in "numbers" are integers
    if not all(isinstance(num, int) for num in numbers):
        return jsonify({'message': 'All elements in "numbers" should be integers'}), 400
    
    # Calculate the median
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "token" key containing the token of the new user.
    '''
    # Check if the "username" parameter is present
    username = request.json.get('username')
    if username is None:
        return jsonify({'message': 'Missing "username" parameter'}), 400
    
    # Check if the username is already taken
    if User.query.get(username):
        return jsonify({'message': 'Username already taken'}), 400
    
    # Create a new user
    token = secrets.token_hex()
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'token': token})
    
    
    