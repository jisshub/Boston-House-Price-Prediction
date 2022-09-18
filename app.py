import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd
import numpy as np
import json
from json import JSONEncoder
# create app
app = Flask(__name__)

# load pickle file
regression_model = pickle.load(open('reg_model.pkl', 'rb'))
scaling_model = pickle.load(open('scaling.pkl', 'rb'))

# create route for home page. By default when we hit the url, it navigates to the home page.
@app.route('/')
def home():
    return render_template('home.html')

# api for prediction. use post request since we give the inputs from our side, 
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data'] 
    new_data=scaling_model.transform(np.array(list(data.values())).reshape(1,-1))
    output=regression_model.predict(new_data)
    print(output[0][0])
    return jsonify(output[0][0])

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input = scaling_model.transform(np.array(data).reshape(1,-1))
    output = regression_model.predict(final_input)[0][0]
    print(output)
    return render_template('home.html', prediction_text=f"The house price prediction is {output}")
    
if __name__ == "__main__":
    app.run(debug=True)





