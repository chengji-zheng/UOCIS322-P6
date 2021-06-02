# Adopted Based On website.example.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# fileType = request.form.get("format") # Get File Type fetched from clientSide
# qty = request.form.get("qty")    # get the quantity from the clientSide


@app.route('/')
@app.route('/index')
def home():
    return render_template('website.html')


@app.route('/listAll')
def listAll():
    app.logger.setLevel("First Line of ListAll")
    fileType = request.args.get("format") # Get File Type fetched from clientSide
    qty = request.args.get("qty")    # get the quantity from the clientSide
    r = requests.get('http://restapi:5000/listAll' + "/" + fileType)
    return r.text

@app.route('/listOpenOnly')
def listOpenOnly():
    fileType = request.args.get("format") # Get File Type fetched from clientSide
    qty = request.args.get("qty")    # get the quantity from the clientSide
    r = requests.get('http://restapi:5000/listOpenOnly' + "/" + fileType + "?top=" + qty)
    return r.text

@app.route('/listCloseOnly')
def listCloseOnly():
    fileType = request.args.get("format") # Get File Type fetched from clientSide
    qty = request.args.get("qty")    # get the quantity from the clientSide
    r = requests.get('http://restapi:5000/listCloseOnly' + "/" + fileType + "?top=" + qty)
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
