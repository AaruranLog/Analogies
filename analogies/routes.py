# coding: utf-8
"""
    App URLs
"""
from flask import render_template, request
from analogies import app
from analogies.backend.word_vectors import Model


@app.route('/')
def root():
    return render_template("base.html", title='Home')


@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/references')
def references():
    git_link = 'https://github.com/AaruranE/Analogies'
    megatutorial_link = "https://blog.miguelgrinberg.com/" \
                        "post/the-flask-mega-tutorial-part-i-hello-world"
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
    brown_model = Model("analogies/backend/brown-20171221.vec")
    word_embedding = brown_model.lookup(text)
    if word_embedding is None:
        display = [f"{text} is not in the vocabulary"]
    else:
        display = word_embedding.tolist()
    return render_template("word-embedding.html", output=display)


@app.route('/brown/analogy')
def brown_analogy():
    return render_template("analogy.html")


@app.route('/brown/analogy', methods=['POST'])
def brown_analogy_post():
    word1 = request.form['word1']
    target1 = request.form['target1']
    word2 = request.form['word2']

    # TODO: Write "latest_model" function, to wrap a regex file search"
    brown_model = Model("analogies/backend/brown-20171221.vec")
    target2 = brown_model.analogy(word1, target1, word2)

    if target2 is None:
        target2 = "***We can't solve this analogy. Corpus vocabulary is too small."

    return render_template("analogy.html", output=target2)  # placeholder as we debug UI
