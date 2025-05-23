import secrets

from flask import Flask, session
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    Get the "username" and "password" from the request body and check if the user/password combination exists in the database.
    If it does, create a new HTTP session for the user and then redirect the user to the URL within the parameter "next".
    If the login is unsuccessful, render the login.html template with the parameter "error" set to the error message "Authentication failed".
    @return: the rendered login.html template or an HTTP redirect to the URL within the parameter "next".
    '''

    if request.method == 'POST':
        # Get the username and password from the request body
        username = request.form['username']
        password = request.form['password']
    
        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()
    
        if user is None or not user.password == password:
            # Authentication failed
            return render_template('login.html', error='Authentication failed')
    
        # Create a new HTTP session for the user
        session['username'] = username
    
        # Redirect the user to the URL within the parameter "next" if it exists, otherwise redirect to the home page
        next_url = request.args.get('next')
        return redirect(next_url or url_for('home'))
    
    # Render the login.html template
    return render_template('login.html')
