

#!pip install flask-ngrok

import os

template_dir = os.path.abspath('/content/drive/MyDrive/Colab Notebooks/complete/run flask on colab/templates')

os.listdir('/content/drive')

from flask_ngrok import run_with_ngrok
from flask import Flask
from flask import render_template

#running the flask app
app = Flask(__name__, template_folder=template_dir)

#we need to start ngrok when the app run

run_with_ngrok(app)
@app.route('/')

def hello_world(): 
    return 'Hello, This is roman!'

@app.route('/h')

def func2(): 
    return 'Hello, This is second page !'





@app.route('/hello/')
def hello():
    return render_template('hello.html')

app.run()

