from flask import Flask, request
import logging
import os

app = Flask(__name__)

os.makedirs("/app/logs", exist_ok=True)

logging.basicConfig(
    filename="/app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.before_request
def log_request_info():
    logging.info(f"{request.method} {request.path} from {request.remote_addr}")

@app.route("/")
def hello():
    return "Hello from Foodly in Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

