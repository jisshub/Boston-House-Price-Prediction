# Boston-House-Price-Prediction

Video Link: https://www.youtube.com/watch?v=MJ1vWb1rGwM&list=PLT6wrBlkasCNqKnKcs1hOoCEhtcUZiAqo&index=100

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

```py
data = request.json['data']
```
This means input we gave will be in json format which then will be captured inside data key.


## Run app.py file on terminal

```bash
python app.py
```

## Testing the app in postman

API: POST http://127.0.0.1:5000/predict_api

```json
{
    "data": {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.0900,
        "RAD": 1.0,
        "TAX": 296,
        "PTRATIO": 15.3,
        "B": 396.90,
        "LSTAT": 5
    }
}
```

## Prediction from Front End Application

1. Create a function in *app.py* file to get the user inputs.

- Once we click the **predict** button, it hits the **predict** url in app.py file. 

- We take all the values from the form.

- Convert them to an array with another shape.

- Finally predicting it to get the output.

- Display the output in an html file.

**app.py**

```py
@app.route('/predict', methods=['POST'])
def predict():
    # capture the form values & convert to float values.
    data=[float(x) for x in request.form.values()]
    # scale and transform the data.
    final_input = scaling_model.transform(np.array(data).reshape(1,-1))
    # predict the output using the inputs which will be a 2D array. we take out the first dimension which gave us the output.
    output = regression_model.predict(final_input)[0][0]
    print(output)
    # render the predicted value in html page.
    return render_template('home.html', prediction_text=f"The house price prediction is {output}")

```

## Procfile for Heroku Deployment

- Create a *Procfile* before deploying the app to heroku.
- A *Procfile* specify some commands that needs to be executed by the app as soon as it starts.


```Procfile
web: gunicorn app:app
```

- **gunicorn** is a python http server for wsgi application.
- Also udpate the *requirements.txt* file with gunicorn.


```txt
Flask
sklearn
pandas
numpy
matplotlib
gunicorn
```

## Deploying The App To Heroku

- Heroku account
- Create new app.
- Choose github cli
- Search for github repository.
- Click on connect.
- Enable Automatic deploys option.
- Click on Deploy Branch button.

## Deploying the app to Dockers

### 1. Create a docker file in root folder. 

### 2. Create a docker image.

    Here with the help of docker file, we create a docker image using the information we write in docker file. That docker image can be taken and run with in a container which will be interacting with the kernel of our OS. Docker is like a container which can be independently run by communicating with the kernel of the OS.

    To create a docker image, we use following commands.
        - FROM
        - COPY
        - WORKDIR
        - RUN
        - EXPOSE
        - CMD

#### 1. FROM Command
    - FROM command is used to select the base image. Docker containers require base image. Base image means we have a Linux OS, on top of that we install other OS.
    
    ```Dockerfile
    FROM python:3.9
    ```

    - When we are building this docker image, it will go and take the baseImage from the docker hub. I.e. it will take a linux based image and on top of that it will install python3.9 and does the other configuration settings.

    - In Short, as soon as docker sees python3.9, from the DockerHub, it takes the baseImage which has Linux on top of it python3.9 and then it does the next step which is COPY.

#### 2. COPY Command

    COPY means whatever files i have in our remote repository, we have to copy them into that baseImage. For that, we copy from current location to a new location in our baseImage. 

    ```Dockerfile
    COPY . /app
    ```
    
    We copy the contents from the current folder to an app folder within our baseImage. The next step is to create that app folder as our working directory.


#### 3. WORKDIR Command

    ```Dockerfile
    WORKDIR /app
    ```

    - We made our app direcotry in baseImage as our working directory.

#### 4. RUN Command

    ```Dockerfile
    RUN pip install -r requirements.txt
    ```

    - Install the packages in requirements.txt file.

#### 5. EXPOSE Command

    ```Dockerfile
    EXPOSE $PORT
    ```

    When docker image run as a container, in order to access the application inside the container, we have to expose some PORT. Then only we can access that entire URL and also from that PORT we are able to access the entire application. So we expose a PORT with in that docker container. $PORT is given because this value when deployed into cloud or server, server is going to automatically assign this port in that container.


#### 6. CMD Command

    <!-- time: 2:31:00 -->





    

















