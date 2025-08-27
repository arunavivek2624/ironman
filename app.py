from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return {"message": "Hello from Ironman running in Docker!", "status": "online"}

@app.route("/health")
def health():
    return {"status": "healthy", "project": "ironman"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)