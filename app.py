import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index(status='status'):
    status = request.cookies.get('status')
    return render_template('index.html', status=status)

@app.route('/power-on', methods=['POST', 'GET'])
def on():
    if request.method == 'POST':
        os.system("sudo uhubctl -l 1-1 -p 2 -a 1")

    resp = redirect(url_for('index'))
    resp.set_cookie('status', 'on')
    return resp 

@app.route('/power-off', methods=['POST', 'GET'])
def off():
    if request.method == 'POST':
        os.system("sudo uhubctl -l 1-1 -p 2 -a 0")

    resp = redirect(url_for('index'))
    resp.set_cookie('status', 'off')
    return resp 

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, host='0.0.0.0', port='5000')
