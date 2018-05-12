from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config.from_pyfile('config.py')
Bootstrap(app)

from views import *

if __name__ =='__main__':
	app.run(host ='0.0.0.0')