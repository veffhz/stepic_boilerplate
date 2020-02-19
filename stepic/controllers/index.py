from flask import request, render_template, flash

from stepic import app


@app.route('/')
def index():
    for arg in request.args.getlist('toast'):
        if arg:
            flash(arg)
    return render_template('index.html')


@app.route('/foo/<bar>')
def foo(bar):
    return f"Foo {bar}"
