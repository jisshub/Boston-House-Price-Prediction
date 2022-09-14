import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd
import numpy as np

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
@app.route('/predict_api', methods=['POST'])
def predict_api():
    # send request in json, store the response in data variable.
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    # get new transformed data
    transformed_data = scaling_model.transform(np.array(list(data.values())).reshape(1,-1))
    # predict w.r.t new data.
    output = regression_model.predict(transformed_data)
    print(output[0])
    # return the output as a json data.
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)





