from flask import Flask
from flask_cors import CORS


app = Flask(__name__, static_url_path='', static_folder='../irrigation-ui/build')
CORS(app)

import application.controllers.Irrigation
