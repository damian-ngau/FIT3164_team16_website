from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Patient
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
	return render_template("home.html", user=current_user)

