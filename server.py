import sys, os
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

REPO_NAME = "sanjaysalem17.github.io"
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
	return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

#URL Routing - Home Page
@app.route("/")
def index():
	return render_template('index.html', pages=pages)

@app.route("/about/")
def about():
	return render_template('home-2.html', page=pages)

@app.route("/game-dev/")
def game():
	return render_template('game.html', page=pages)

@app.route("/graphic-design/")
def graphic():
	return render_template('graphic.html', page=pages)

@app.route("/animation/")
def animation():
	return render_template('animation.html', page=pages)

@app.route("/contact/")
def contact():
	return render_template('contact.html', page=pages)

@app.route("/coding/")
def coding():
	return render_template('coding.html', page=pages)

# Main Function, Runs at http://0.0.0.0:8000
if __name__ == "__main__":
		freezer.freeze()