from flask import render_template, request
from app import app
from app import backend

@app.route('/')
@app.route('/index')
def index():
	user = dict(username='Visitor')
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/source-code')
def source():
	git_link = 'https://github.com/AaruranE/Analogies'
	return render_template('references.html', title='Source Code', git_link=git_link)


@app.route('/predict')
def predict():
	return render_template('my-form.html')

@app.route('/predict', methods=['POST'])
def predict_post():
	text = request.form('text')
	try:
		value = int(text)
	except ValueError:
		value = None
	return render_template("my-form.html", output=value)

	