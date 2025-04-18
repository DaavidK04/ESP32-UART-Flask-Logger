from flask import Flask, render_template
import threading
import serial

app = Flask(__name__)
log_data = []

def read_uart():
    global log_data
    ser = serial.Serial('/dev/serial0', 115200, timeout=1)
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            log_data.append(line)
            log_data = log_data[-100:]  # Nur die letzten 100 Zeilen behalten

@app.route('/')
def index():
    return render_template('index.html', logs=log_data)

if __name__ == '__main__':
    threading.Thread(target=read_uart, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
