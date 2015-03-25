#!/usr/local/bin/python
import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

#---------- MODEL IN MEMORY ----------------#

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
patients = pd.read_csv("haberman.data", header=None)
patients.columns=['age','year','nodes','survived']
patients=patients.replace(2,0)  # The value 2 means death in 5 years

X = patients[['age','year','nodes']]
Y = patients['survived']
PREDICTOR = LogisticRegression().fit(X,Y)


#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__, static_folder='output',static_url_path='')

# Homepage
@app.route("/")
def home_page():
    return app.send_static_file('index.html')

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])
def score():
    """  When A POST request with json data is made to this uri,
         Read the example from the json, predict probability and
         send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    x = np.matrix(data["example"])
    score = PREDICTOR.predict_proba(x)
    # Put the result in a nice dict so we can send it as json
    results = {"score": score[0,1]}
    return flask.jsonify(results)

app.debug = True

app.run(host='0.0.0.0', port=8080)

