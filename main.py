from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)



@app.route("/")
def get_method():
    return render_template('index.html', name="")

@app.route("/send", methods=["GET"])
def get_method():
    name = "GET!!!"
    return render_template('index.html', name=name)


@app.route("/send", methods=["POST"])
def get_method():
    name = "GET!!!"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)