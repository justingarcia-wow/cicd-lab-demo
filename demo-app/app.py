from flask import Flask
import os, socket

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    return f"Hola desde {socket.gethostname()} - versión {VERSION}\n"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
