import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import sys
import logging


app = Flask(__name__, template_folder='templates')
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
model = pickle.load(open('randomforest_tuned_model_pickle.pkl', 'rb'))

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
	For rendering results on HTML GUI
	'''
    print('Enter input values')
    int_features = [float(x) for x in request.form.values()]
    final_features = pd.DataFrame([int_features])
    final_features.columns=['V22', 'V3', 'V8', 'V11', 'V17', 'V4', 'V14', 'V21', 'V12', 'V7', 'V16', 'V10', 'V13']
    prediction = model.predict_proba(final_features)
    output = prediction[0][1]
    print(output)
    if output > 0.2450:
        return render_template('index.html', prediction_text='PAY ATTENTION PLEASE !!!!!! THIS TRANSACTION SEEMS FRADULENT')
    elif output <= 0.2450:
        return render_template('index.html', prediction_text='EVERYTHING SEEMS OKAY... THIS TRANSACTION SEEMS NON-FRADULENT')
    else:
        return render_template('index.html', prediction_text='Please enter values to the following fields to predict whether the transaction is fradulent or not') 
     


if __name__ == "__main__":
    app.run(debug=True)
    
