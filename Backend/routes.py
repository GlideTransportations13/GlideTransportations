from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from Backend.models import db, Driver, Shipment, User
from Backend.forms import LoginForm
import os

main_routes = Blueprint('main', __name__)

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Ideally use hashed passwords
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@main_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_routes.route('/register_driver', methods=['POST'])
@login_required
def register_driver():
    data = request.json
    driver = Driver(**data)
    db.session.add(driver)
    db.session.commit()
    return jsonify({'message': 'Driver registered successfully!'}), 201

@main_routes.route('/upload_shipment', methods=['POST'])
@login_required
def upload_shipment():
    if 'pictures' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    files = request.files.getlist('pictures')
    uploaded_files = []

    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_files.append(filename)

    data = request.form.to_dict()
    data['pictures'] = uploaded_files  # Store uploaded file names
    shipment = Shipment(**data)
    db.session.add(shipment)
    db.session.commit()
    return jsonify({'message': 'Shipment uploaded successfully!'}), 201

@main_routes.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@main_routes.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500