import sys, os
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
STATIC_DIR = os.path.abspath('/')

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
	return render_template('about.html', page=pages)

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
	app.run()