from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "AWS Monitoring Demo Application is Running!"

@app.route("/health")
def health():
    return "Healthy"

@app.route("/work")
def work():
    total = 0
    for i in range(1000000):
        total += i
    return f"Work completed: {total}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
