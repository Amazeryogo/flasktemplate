from flask import *
import waitress


app = Flask(__name__)


waitress.run(app, host='0.0.0.0',port=5000)
