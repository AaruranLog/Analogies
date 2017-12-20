from flask import Flask

app = Flask(__name__)

from analogies import routes
from analogies import backend