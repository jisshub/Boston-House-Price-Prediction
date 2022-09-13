# Boston-House-Price-Prediction

## Create New Repository

- Clone the repository into our machine.

## Software and Tools Requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://heroku.com)
4. [Git CLI](https://git-scm.com/downloads)

## Create New Environment

```bash
conda create -p venv python==3.9 -y
```

## Activate New Environment

```bash
conda activate env_name
conda init shell
conda info --envs
```

## Create a requirements.txt file

Attach the lirabried we require in this file.

```txt
Flask
sklearn
pandas
numpy
matplotlib
```

Install the libraries using below command,


```bash
pip install -r requirements.txt
```

## Setting up git


```bash
git config --global user.name
git config --global user.email
```

- Create a *.gitignore* file and add the files not required to be pushed to remote repository.

```bash
git add --all
git commit -am "Add All"
git pull && git push
```

## Create a Flask Web Application

Create *app.py* file.

```py
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd
import numpy as np

# create app
app = Flask(__name__)

# load pickle file
regression_model = pickle.load(open('reg_model.pkl', 'rb'))

# create route for home page. By default when we hit the url, it navigates to the home page.
@app.route('/')
def home():
    return render_template('home.html')

# api for prediction. use post request since we give the inputs from our side, 
@app.route('/predict_api', methods=['POST'])
def predict():
    pass
```

<!-- time: 1:44:00 -->




