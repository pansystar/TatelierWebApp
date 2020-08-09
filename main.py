from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def Hello():
    name = "pansystar"
    return app.send_static_file('/index.html')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)