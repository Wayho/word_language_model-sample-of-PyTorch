# coding: utf-8

from datetime import datetime

from flask import Flask

from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def index():
	return 'index'


@app.route('/time')
def time():
	return str(datetime.now())

@app.route('/heart')
def heart():
	return 'Heart'


@sockets.route('/echo')
def echo_socket(ws):
	while True:
		message = ws.receive()
		ws.send(message)
