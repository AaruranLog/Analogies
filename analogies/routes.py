from flask import render_template, request
from analogies import app
from analogies.backend.word_vectors import Model
import numpy as np


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

# TODO: update this route to include Flask Mega-tutorial etc.
@app.route('/source-code')
def source():
	git_link = 'https://github.com/AaruranE/Analogies'
	return render_template('references.html', title='Source Code', git_link=git_link)

@app.route('/predict')
def predict():
	return render_template('my-form.html')

@app.route('/predict', methods=['POST'])
def predict_post():
	text = request.form['text']
	print(f"text:{text}")
	try:
		value = int(text)
		value = str(value ** 2)
		print("squared successfully")
	except:
		print(f"value:{value}")
		value = "Invalid input"

	return render_template("my-form.html", output=value)


@app.route('/brown/word')
def brown_word2vec():
	return render_template('word-embedding.html')

@app.route('/brown/word', methods=['POST'])
def brown_word2vec_post():
	text = request.form['text']
	print(f"text:{text}")

	# TODO: Write "latest_model" function, to wrap a regex file search"
	brown_model = Model("analogies/backend/brown-20171219.model")
	word_embedding = brown_model.lookup(text)
	return render_template("word-embedding.html", output=word_embedding.tolist())





	