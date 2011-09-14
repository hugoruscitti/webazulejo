from flask import Flask, render_template
from app.db import session_remove

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', model=[])


@app.after_request
def shutdown_session(response):
    session_remove()
    return response

