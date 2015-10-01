#!/usr/local/bin/python3
import flask
from sklearn.linear_model import LogisticRegression

import json
import numpy as np
import pandas as pd

from predictor import fit_predict as fp

#---------- MODEL IN MEMORY ----------------#

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
# patients = pd.read_csv("haberman.data", header=None)
# patients.columns=['age','year','nodes','survived']
# patients=patients.replace(2,0)  # The value 2 means death in 5 years
#
# X = patients[['age','year','nodes']]
# Y = patients['survived']
# PREDICTOR = LogisticRegression().fit(X,Y)

franchise_df = fp.complete_df
lin_mod = fp.modelFit(fp.complete_df)

franchise_df['act_gross'] /= 10**6
franchise_df['prev_gross'] /= 10**6

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

@app.route("/data", methods=["GET"])
def data():
    data = franchise_df[['days_elapsed','act_gross','first_title','new_title','prev_gross']].dropna()
    return data.to_json(orient = 'records')

app.debug = True

app.run(host='127.0.0.1', port=8080)


