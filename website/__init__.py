from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secretkey'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rxntztzcimolbf:b9552a4087845273bf0780ee1d607ce4aa5aeffc6fdec1edacbffb7607eada6c@ec2-52-207-47-210.compute-1.amazonaws.com:5432/d8jmp9cuqupt0l'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Patient, Result

	create_database(app)
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
	if not path.exists('website/' + DB_NAME):
		db.create_all(app=app)

