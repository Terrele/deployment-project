# import Flask and jsonify
from flask import Flask, jsonify, request, render_template
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    
    data = request.get_json()
    df = pd.DataFrame.from_dict(data)
    
    prediction = model.predict(df)
    output = prediction.tolist()

    return jsonify(output) 
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
