from app import myapp_obj
from app.models import User
from app.models import Post
from app import db

from flask import render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
#----------------------------------------------------------------------------#
class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')
class SignUpForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
class DeleteAccount(FlaskForm):
    delete = SubmitField('Delete')
class addPost(FlaskForm):
    post = StringField('Post', validators=[DataRequired()])
class buyForm(FlaskForm):
    cardNumber = StringField('Buy with Credit Card:', validators=[DataRequired()])
    submit = SubmitField('Buy')
    user = 0
    post = 0
class searchForm(FlaskForm):
    query = StringField('Post', validators=[DataRequired()])
    submit = submit = SubmitField('Search')
#----------------------------------------------------------------------------#
@myapp_obj.route("/SignUp", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = SignUpForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        user = User.query.filter_by(username=form.username.data).first()
        if user or email:
            flash('User or Email already taken')
        else:
            hashed_password = generate_password_hash(form.password.data)
            user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html', title='SignUp', form=form)


@myapp_obj.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            next = request.args.get('next') #Prevents illegal redirects
            return redirect(next or url_for('profile'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login',form=form)

@myapp_obj.route("/")
def splash():
    return render_template('splash.html', title='Splash')

@myapp_obj.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    return render_template('home.html')

@login_required
@myapp_obj.route('/profile', methods=['GET', 'POST'])
def profile():
    user = User.query.filter_by(username=current_user.username).first()
    email = user.email
    form = addPost()
    post = user.posts
    if request.method == 'POST':
        post = Post(body=form.post.data, timestamp=datetime.utcnow(), user_id=user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post added!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user, email=email, form=form, post=post)

@myapp_obj.route('/all', methods=['GET','POST'])
def all():
    forms = []
    users = db.session.query(User).all()
    for user in users:
        for post in user.posts:
            forms.append(buyForm())
            forms[len(forms)-1].user = user
            forms[len(forms)-1].post = post
    for form in forms:
        if form.validate_on_submit():
            Post.query.filter_by(timestamp=form.post.timestamp).delete()
            db.session.commit()
            return redirect(url_for('all'))
    
    return render_template('all.html', forms=forms)

@myapp_obj.route('/search', methods=['GET','POST'])
def search():
    search = searchForm()
    forms = []
    if search.validate_on_submit():
        users = db.session.query(User).all()
        for user in users:
            for post in user.posts:
                if post.body.__eq__(search.query.data):
                    print(post.body)
                    print(search.query)
                    forms.append(buyForm())
                    forms[len(forms)-1].user = user
                    forms[len(forms)-1].post = post

        for form in forms:
            if form.validate_on_submit():
                Post.query.filter_by(timestamp=form.post.timestamp).delete()
                db.session.commit()
                return redirect(url_for('home'))
            
    return render_template('search.html', search=search, forms=forms)

@myapp_obj.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logging out...', 'success')
    return redirect('home')

@myapp_obj.route("/deleteAccount", methods=['GET','POST'])
@login_required
def deleteAccount():
    form = DeleteAccount()
    if request.method == 'POST':
        current_user.delete()
        db.session.commit()
        flash('Deleted Account', 'success')
        return redirect('home')
    return render_template('delete.html',form=form)
