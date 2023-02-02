# from flask import render_template, session, redirect, url_for, flash
# from flask_login import login_required
#
# from config.app_constants import USERNAME
# from services.user_services import app, db
# from utils.send_email import send_otp_mail
#
#
# @app.route('/registration')
# def registration_form():
#     return render_template('registration.html')
#
#
# @app.route('/login')
# def login_template():
#     return render_template('login.html')
# @app.route('/logged_in')
# @login_required
# def logged_in_template():
#     return render_template('logged_in.html')
#
#
# @app.route('/two_fa_login_template')
# def two_fa_login_template():
#     if USERNAME not in session:
#         return redirect(url_for('app.login'))
#     user = db.get_user(username=session[USERNAME])
#     if user is None:
#         flash('something went wrong')
#         return redirect(url_for('app.login'))
#     db.update_user(user="franco", otp=send_otp_mail())
#     return render_template('otp.html')
#
#
# @app.route('/example')
# @login_required
# def example():
#     return render_template('example.html')