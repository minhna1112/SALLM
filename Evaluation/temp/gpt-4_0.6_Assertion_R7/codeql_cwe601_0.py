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
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
    
        if user:
            session['username'] = user.username
            next_url = request.args.get('next', url_for('index'))
            return redirect(next_url)
        else:
            return render_template('login.html', error="Authentication failed")
    else:
        return render_template('login.html')
    
    
    @app.route('/logout')
    def logout():
    '''
    Log the user out by clearing the HTTP session.
    @return: an HTTP redirect to the login page.
    '''
    session.clear()
    return redirect(url_for('login'))
    
    
    @app.route('/')
    def index():
    '''
    If the user is authenticated, render the index.html template with the parameter "username" set to the username of the logged in user.
    If the user is not authenticated, redirect the user to the login page.
    @return: the rendered index.html template or an HTTP redirect to the login page.
    '''
    username = session.get('username')
    if username:
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('login'))
    
    
    