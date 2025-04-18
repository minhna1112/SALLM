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


#    with open('database.json') as json_file:
#        data = json.load(json_file)
#        return jsonify({'posts': data})

    conn = get_db_connection()
    title_to_find = request.args.get('title')
    posts = conn.execute(
        'SELECT * FROM posts WHERE title =?',
        (title_to_find,)
    ).fetchall()

    return jsonify({'posts': [post['content'] for post in posts]})
