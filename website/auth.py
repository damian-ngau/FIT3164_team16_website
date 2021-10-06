from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Patient, Result
# coverts password so that it does not store password as plain text, generates a hash
# the password that is typed in MUST be equal to the hash that is stored
# sha256 is the hashing algorithm
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from keras.models import load_model
from keras.preprocessing import image


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		email = request.form.get('email')
		first_name = request.form.get('firstName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		user = User.query.filter_by(email=email).first()
		if user:
			flash('Email already exists.', category='error')
			return render_template("sign_up.html", user=current_user)
		if len(email) < 4:
			flash('Email must be greater than 3 characters.', category='error')
			return render_template("sign_up.html", user=current_user)
		elif len(first_name) < 2:
			flash('First name must be greater than 1 character.', category='error')
			return render_template("sign_up.html", user=current_user)
		elif password1 != password2:
			flash('Passwords don\'t match.', category='error')
			return render_template("sign_up.html", user=current_user)
		elif len(password1) < 7:
			flash('Password must be at least 7 characters.', category='error')
			return render_template("sign_up.html", user=current_user)
		else:
			new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember=True)
			flash('Account created!', category='success')
			return redirect(url_for('views.home'))

	return render_template("sign_up.html", user=current_user)

@auth.route('/create_patient', methods=['GET', 'POST'])
@login_required
def create_patient():
	if request.method == 'POST':
		first_name = request.form.get('firstName')
		if len(first_name) < 2:
			flash('First name must be greater than 1 character.', category='error')
		else: 
			new_patient = Patient(first_name=first_name, user_id=current_user.id)
			db.session.add(new_patient)
			db.session.commit()
			flash('Patient created!', category='success')
			return redirect(url_for('views.home'))

	return render_template("create_patient.html", user=current_user)


@auth.route('/result_history/<int:patient_id>')
@login_required
def result_history(patient_id):
	patient = Patient.query.get_or_404(patient_id)
	return render_template("result_history.html", patient=patient, user=current_user)


@auth.route('/save_result', methods=['GET', 'POST'])
@login_required
def save_result():
	if request.method == 'POST':
		# select a patient ID
		selected_patient = request.form.get('patientID')
		
		# percentage of the cancer image
		cancer_percentage = request.form.get('percentage')
		
		# note created by user
		add_note = request.form.get('note')
		

		# user has not uploaded image, redirect to home page
		if cancer_percentage==" ":
			flash('No Image Submitted', category='error')
		else: 
			new_result = Result(note=add_note, percentage=cancer_percentage, patient_id=selected_patient)
			db.session.add(new_result)
			db.session.commit()
			flash('Saved Result', category='success')
			return redirect(url_for('views.home'))
	return render_template("upload_image.html", user=current_user)



@auth.route('/upload_image', methods=['GET', 'POST'])
@login_required
def upload_image():
	return render_template("upload_image.html", user=current_user)

########################
########################
########################
# machine learning model

model = load_model('best_model.h5')

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(200,200))
	i = image.img_to_array(i) 
	i = i.reshape(1, 200,200,3)
	p = model.predict(i)
	return p

@auth.route("/get_output", methods = ['GET', 'POST'])
@login_required
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		show_image = "static/" + img.filename

		img_path = "website/static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)
		labels = ['MSI', 'MSS']

		if p[0][0]>p[0][1]:
			pred_perc = str(round(p[0][0] * 100, 2)) + '%'
			# print(pred_perc)
			pred_lab = labels[0]

		if p[0][0]<p[0][1]:
			pred_perc = str(round(p[0][1] * 100, 2)) + '%'
			# print(pred_perc)
			pred_lab = labels[1]
	return render_template("upload_image.html", user=current_user, pred_perc = pred_perc, pred_lab = pred_lab, show_image = show_image)
