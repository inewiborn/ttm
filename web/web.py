from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """hello page"""
    return 'Hello world from Flask!'


app.run()
