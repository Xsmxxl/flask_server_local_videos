#!/usr/bin/env python
from flask import Flask, render_template


app = Flask(__name__, static_folder='static')

@app.route('/video/<id>')
def index(id):
    dato="video"+id+".mkv"
    return render_template('index.html', prueba=dato)

if __name__ == '__main__':
    app.run(host='192.168.0.22', port='5000', debug=False, ssl_context=('cert.pem', 'key.pem'))