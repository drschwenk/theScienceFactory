#!/usr/local/bin/python2
from flask import Flask, request, render_template, send_from_directory, Response
import json
from flavorNetwork.recommender import FlavorRecommender
from flavorNetwork.load_data import load_data


# Initialize the app
app = Flask(__name__, static_folder='output', static_url_path='', template_folder='output')

#load data and initialize recommender
data_dir = './pkld_data/'
comp_ing_dict, edge_dict, all_recipes, pre_match_dict = load_data(data_dir)
comptail_recommender = FlavorRecommender(comp_ing_dict, edge_dict, all_recipes, pre_match_dict)
new_drink = ['gin','lemon', 'cucumber']

# Homepage
@app.route("/")
def home_page():
    return app.send_static_file('index.html')


@app.route('/recommender', methods=['GET', 'POST'])
def index():
    query = request.form.get('ingredients', None)

    if not query or (query is not None and len(query) == 0):
        query = "Enter ingredients separated by commas..."

    if query is not None:
        recommendation = comptail_recommender.make_rec(query, 15)
        # recommendation = query
        print recommendation
        return render_template('recommend.html', query=query, recommendation=recommendation)
    print 'here'
    return render_template('recommend.html', query=query)

app.debug = False

app.run(host='127.0.0.1', port=8080)


