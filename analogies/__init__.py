"""init for analogies app"""
from flask import Flask
from analogies.utils.config import Config
from analogies import routes
from analogies import backend

app = Flask(__name__)
app.config.from_object(Config)
