from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def Hello():
    name = "pansystar"
    return "Hello"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)