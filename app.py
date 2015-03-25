import flask
# Initialize the app
app = flask.Flask(__name__, static_folder='output',static_url_path='')

# Homepage
@app.route("/")
def home_page():
    return app.send_static_file('index.html')

app.debug = True

app.run(host='0.0.0.0', port=8080)

