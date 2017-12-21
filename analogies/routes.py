from flask import render_template, request
from analogies import app
from analogies.backend.word_vectors import Model
import numpy as np


@app.route('/')
def root():
    return render_template("base.html", title='Home')


@app.route('/index')
def index():
    return render_template('index.html', title='Home')


# TODO: update this route to include Flask Mega-tutorial etc.
@app.route('/references')
def references():
    git_link = 'https://github.com/AaruranE/Analogies'
    megatutorial_link = "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world"
    sources = [
        {
            "link":git_link,
            "name":"Source Code"
        },
        {
            "link": megatutorial_link,
            "name": "The Flask Mega-Tutorial"
        }
    ]

    return render_template('references.html', sources=sources)


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
    brown_model = Model("analogies/backend/brown-20171221.model")
    word_embedding = brown_model.lookup(text)
    return render_template("word-embedding.html", output=word_embedding.tolist())
