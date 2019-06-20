from flask import Flask
from entertainmentCrossing.config import Config

def create_app(config_class=Config):
	

	app = Flask(__name__)

	with app.app_context():
		app.config.from_object(Config)

		from entertainmentCrossing import routes

	return app