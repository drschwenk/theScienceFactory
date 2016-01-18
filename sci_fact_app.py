#!/usr/local/bin/python2
from flask import Flask, request, render_template, send_from_directory, Response
import json

# Initialize the app
app = Flask(__name__, static_folder='output',static_url_path='', template_folder='output')

# Homepage
@app.route("/")
def home_page():
    return app.send_static_file('index.html')

@app.route('/recommender', methods=['GET', 'POST'])
def index():
    query = request.form.get('ingredients', None)
    print query

    if query is not None and len(query) == 0:
        query = None

    # if query is not None:
    #     recommendation = query
    #     return render_template('recommend.html', query=query, recommendation=recommendation)
    print 'here'
    return render_template('recommend.html')

app.debug = True

app.run(host='127.0.0.1', port=8080)


