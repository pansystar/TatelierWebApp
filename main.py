from flask import Flask, render_template, request, jsonify
import pandas as pd
from sqlalchemy import create_engine
import os

app = Flask(__name__)



@app.route("/")
def hello():
    engine = create_engine('postgres://ozqqhdmuqezsca:a220c425e3f1a1ab567bdfb15625642cd33f3ca924a3846352923f45bf39d6ba@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d4p1h3ane0mls4')  
    df = pd.read_sql(sql='select * from pansydb;', con=engine)
    return render_template('index.html', name=df)

@app.route("/send", methods=["GET"])
def get_method():
    name = "GET!!!"
    return render_template('index.html', name=name)

@app.route("/send", methods=["POST"])
def post_method():
    # インサートする
    iD = request.form['id']
    age = request.form['age']
    name = request.form['name']

    engine = create_engine('postgres://ozqqhdmuqezsca:a220c425e3f1a1ab567bdfb15625642cd33f3ca924a3846352923f45bf39d6ba@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d4p1h3ane0mls4')  
    # df = pd.read_sql(sql='insert into pansydb (id, user_name, age) values ('+ iD +', \'' + name + '\', '+ age +');', con=engine)
    
    return render_template('index.html', name="OK")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)