import psutil
from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    cp = psutil.cpu_percent()
    mp = psutil.virtual_memory().percent
    Message = None
    if cp > 80 or mp > 80:
        Message = "High"
    return f'CPU: {cp} and Memory: {mp}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
