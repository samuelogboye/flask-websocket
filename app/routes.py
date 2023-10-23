from flask import render_template, request, jsonify
from app import app, socketio

@app.route('/')
def index():
    return render_template('index.html')

# @socketio.on('message')
# def handle_message(message):
#     print('Received message:', message)
#     socketio.emit('response', 'Message received: ' + message)
@socketio.on('chat_message')
def handle_chat_message(message):
    socketio.emit('chat_message', message)


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
