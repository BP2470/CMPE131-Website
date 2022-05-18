from app import myapp_obj
from app.models import User
from app.models import Post
from app import db

from flask import render_template, flash, redirect, url_for, request, send_file
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FormField, IntegerField, SelectField
from wtforms.validators import DataRequired

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import string, random, os
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
    item = StringField('Post', validators=[DataRequired()])
    price = IntegerField('Item price:', validators=[DataRequired()])
    is_auction = BooleanField('Set item to auction?:')
    file = FileField(validators=[FileRequired()])
    rating = IntegerField('rating')
class buyForm(FlaskForm):
    cardNumber = IntegerField('Buy with Credit Card:', validators=[DataRequired()])
    submit = SubmitField('Buy')
    user = 0
    post = 0
class searchForm(FlaskForm):
    choices = [('Users', 'Users'), ('Products', 'Products')]
    select = SelectField('Search for:', choices=choices)
    query = StringField('', validators=[DataRequired()])
    submit = SubmitField('Search')
#----------------------------------------------------------------------------#
def get_random_string(length):
    # Combination of lower and upper
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
#----------------------------------------------------------------------------#
@myapp_obj.route("/SignUp", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.username, id=current_user.id))
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
        return redirect(url_for('profile', username=current_user.username, id=current_user.id))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            next = request.args.get('next') #Prevents illegal redirects
            return redirect(next or url_for('profile', username=current_user.username, id=current_user.id))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login',form=form)


@myapp_obj.route("/")
def splash():
    return render_template('splash.html', title='Splash')


@myapp_obj.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.username, id=current_user.id))
    return render_template('home.html')

@login_required
@myapp_obj.route('/profile/<username>_<id>', methods=['GET', 'POST'])
def profile(username, id):
    user = User.query.filter_by(username=current_user.username).first()
    page_owner = User.query.filter_by(username=username).first()
    email = user.email
    form = addPost()
    post = user.posts
    if request.method == 'POST' and form.validate():
        f = form.file.data
        rating = form.rating.data
        fn = secure_filename(f.filename) #Just adding actual name of image
        ext = os.path.splitext(fn)[1]
        new_filename = get_random_string(20) #Ensures no duplicate images
        new_name = new_filename+ext
        f.save(os.path.join(myapp_obj.config['IMAGEFOLDER'], new_name))
        post = Post(body=form.item.data, price=form.price.data, filename = fn, filelink=new_name, is_auction=0, timestamp=datetime.utcnow(), user_id=user.id, in_cart=False, rating=rating)
        if form.is_auction.data == True:
            post.is_auction = 3
        db.session.add(post)
        db.session.commit()
        flash('Post added!', 'success')
        return redirect(url_for('profile', username=current_user.username, id=current_user.id))
    return render_template('profile.html', user=user, page_owner=page_owner, form=form, post=current_user.posts)


@myapp_obj.route('/all', methods=['GET','POST'])
def all():
    users = db.session.query(User).all()
    return render_template('all.html', users=users)


@myapp_obj.route('/search', methods=['GET','POST'])
def search():
    search = searchForm()
    if request.method == 'POST' and search.validate():
        if search.select.data == 'Users':
            user = User.query.filter_by(username=search.query.data).first()
            return render_template('search.html', search=search, user=user)
        else:
            posts = Post.query.filter_by(body=search.query.data).all()
            def getUser(id):
                return User.query.get(id)
            return render_template('search.html', search=search, posts=posts, getUser=getUser)
    return render_template('search.html', search=search)

@myapp_obj.route('/item/id:<item_id>', methods=['GET', 'POST'])
def item_page(item_id):
    
    if item_id == None:
        return render_template('item.html')
    else:
        item = Post.query.get(item_id)
        item_form = buyForm()
        item_form.user = User.query.get(item.user_id)
        item_form.post = item
        
        if request.method == 'POST' and item_form.validate():
            if item.is_auction > 0:
                if item_form.cardNumber.data > item.price:
                    item.is_auction -= 1
                    item.price = item_form.cardNumber.data
                    db.session.commit()
                else:
                    flash('Bid price too low.')
            else:
                db.session.delete(item)
                db.session.commit()
                return redirect(url_for('home'))
        
        
        return render_template('item.html', item_form=item_form)


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
    if request.method == 'POST' and form.validate():
        current_user.delete()
        db.session.commit()
        flash('Deleted Account', 'success')
        return redirect('home')
    return render_template('delete.html',form=form)

@myapp_obj.route("/search", methods=['GET', 'POST'])
@login_required
def searchItem():
    form = searchItem()
    user = db.session.query(User).all()
    email = user.email
    items = []
    post = user.posts
    if form.validate_on_submit():
        for x in user:
            for y in user.post:
                if(post.body.__eq__(post.body)):
                    items.append(post)
                else:
                    flash('Item not found')
