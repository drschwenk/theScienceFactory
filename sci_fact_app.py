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
    button_message = "Enter ingredients separated by commas..."
    if not query or (query is not None and len(query) == 0):
        query = button_message

    if query is not None and query != button_message:
        print 'here'
        recommendations = comptail_recommender.make_rec(query, 15)
        recs = [rec[0] for rec in recommendations]
        insps = [rec[1] for rec in recommendations]
        print recs, insps
        return render_template('recommend.html', query=query, rec1=recs[0], insp1=insps[0],
                                                              rec2=recs[1], insp2=insps[1],
                                                              rec3=recs[2], insp3=insps[2],
                                                              rec4=recs[3], insp4=insps[3])
    return render_template('recommend.html', query=query)

app.debug = True

app.run(host='127.0.0.1', port=8080)


