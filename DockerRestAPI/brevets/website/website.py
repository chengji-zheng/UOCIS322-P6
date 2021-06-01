# Adopted Based On website.example.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

fileType = request.form.get("format") # Get File Type fetched from clientSide
qty = request.form.get("qty")    # get the quantity from the clientSide


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/listAll', methods=["POST"])
def listeverything():
    r = requests.form.get('http://restapi:5000/listAll' + "/" + fileType)
    return r.text

@app.route('/listOpenOnly', methods=["POST"])
def listeverything():
    r = requests.get('http://restapi:5000/listOpenOnly' + "/" + fileType + "?top=" + qty)
    return r.text

@app.route('/listCloseOnly', methods=["POST"])
def listeverything():
    r = requests.get('http://restapi:5000/listCloseOnly' + "/" + fileType + "?top=" + qty)
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
