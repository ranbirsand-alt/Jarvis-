from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>JARVIS AI</h1>
    <p>Your assistant is ready!</p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "JARVIS is running"})

if __name__ == "__main__":
    app.run()
