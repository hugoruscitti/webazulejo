from flask import Module, render_template

project = Module(__name__)

@project.route('/')
def index():
    return render_template('project.html', model=[])

