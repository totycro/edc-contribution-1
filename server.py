from flask import Flask, escape, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""<html>
    <h1>EDC App Contribution Demonstration</h1>

    This application has been launched with the following environment variables:
    <ul>
        {"".join("<li>" + key + "</li>" for key in os.environ)}
    </ul>

    </html>
    """

