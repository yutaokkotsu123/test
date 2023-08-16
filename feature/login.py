from flask import Blueprint,request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required
from models.user_login import Register
# from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db


auth = Blueprint('auth', __name__,
                template_folder='templates',
                static_folder='static')



@auth.route('/signup')
def signup():
    return render_template('signup.html')
@auth.route('/signup', methods = ["POST", "GET"])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')  
    check_user_exist = Register.query.filter_by(email=email).first()
    if check_user_exist:
        flash('Account already exist !')
        return redirect(url_for('auth.signup'))
    new_user = Register(username=username, password=password,
                        email=email, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()
    flash('Check your email or password !')
    return redirect(url_for('auth.login'))
    
    
@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/login', methods = ["POST", "GET"])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = Register.query.filter_by(email=email).first()
    if user: 
        if user.password==password:
            login_user(user)
            return redirect(url_for('initial'))
        else:
            flash('Check your email or password !')
            return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))