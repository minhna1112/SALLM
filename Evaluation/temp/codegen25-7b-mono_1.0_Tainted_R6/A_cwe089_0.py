import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''

    db = get_db_connection()
    account = request.args.get('title')
    post = db.execute('SELECT * FROM post WHERE title = :name',
                        {'name': account}).fetchone()
    db.close()
    return render_template('post.html', post=post)
