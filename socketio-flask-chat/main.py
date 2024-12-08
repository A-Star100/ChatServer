from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Handle messages sent by the client
@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    send(msg, broadcast=True)  # Broadcast the message to all clients

# Start the Flask app with SocketIO on port 5000
if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
