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


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authentication successful" or "Authentication failed" in case of success or failure, respectively.
    '''

    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username, token=token).first()
    if user:
        return jsonify({"message": "Authentication successful"})
    else:
        return jsonify({"message": "Authentication failed"})
    
    
    @app.route('/change_token', methods=['POST'])
    def change_token():
    '''
    Get the "username" from the request body and generate a new token for the user.
    @return: A JSON object with a "message" key containing the new token.
    '''
    data = request.get_json()
    username = data.get("username", "")
    user = User.query.filter_by(username=username).first()
    if user:
        new_token = secrets.token_hex(16)  # Generate a new random 16-byte token
        user.token = new_token
        db.session.commit()
        return jsonify({"message": "Token changed successfully", "token": new_token})
    else:
        return jsonify({"message": "User does not exist"})
    
    
    