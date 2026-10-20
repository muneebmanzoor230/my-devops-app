from flask import Flask, render_template, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', hostname=hostname, time=current_time)

@app.route('/health')
def health():
    # The Load Balancer will check this URL to make sure the app is alive
    return jsonify({
        "status": "healthy",
        "message": "Application is running perfectly!"
    })

if __name__ == '__main__':
    # We use port 8080. 0.0.0.0 means it will accept connections from outside.
    app.run(host='0.0.0.0', port=8080)
