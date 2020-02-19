from stepic import app


@app.route('/')
def index():
    return "Hello World"


@app.route('/foo/<bar>')
def foo(bar):
    return f"Foo {bar}"

