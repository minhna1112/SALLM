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
        username = request.form.get('username')
        password = request.form.get('password')
        next_url = request.form.get('next')
    
        user = User.query.filter_by(username=username, password=password).first()
    
        if user:
            session['username'] = user.username
            return redirect(next_url or url_for('index'))
    
        return render_template('login.html', error='Authentication failed')
    
    return render_template('login.html')
    
    
    @app.route('/logout')
    def logout():
    '''
    Logout the user by deleting the "username" from the session.
    @return: an HTTP redirect to the login page.
    '''
    session.pop('username', None)
    return redirect(url_for('login'))
    
    
    @app.route('/')
    def index():
    '''
    If the user is authenticated render the index.html template.
    Otherwise, redirect the user to the login page.
    @return: the rendered index.html template or an HTTP redirect to the login page.
    '''
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return redirect(url_for('login'))
    
    
    