from flask import render_template, url_for, flash, redirect, request
from movie2archive import app, db, mongo, bcrypt, access_key
from movie2archive.forms import (
    RegistrationForm, LoginForm, MediaCatForm)
from movie2archive.models import User, Movielookup, Media
from flask_login import (
    login_user, logout_user, current_user, login_required)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register.html", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashedpw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashedpw)
        db.session.add(user)
        db.session.commit()
        flash(f'Hey {form.username.data} Your account was created sucessfully,\nYou can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
            user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_redirect = request.args.get('next')
            return redirect(next_redirect) if next_redirect else redirect(
                url_for('dashboard'))
        else:
            flash(f'login failed, Please try again', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", title='Profile')


# testing mongo connection
@app.route("/collection")
@login_required
def collection():
    movies = mongo.db.movies.find()
    return render_template("collection.html", title='Profile', movies=movies)


@app.route("/dashboard")
@login_required
def dashboard():
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this area.', 'warning')
        return redirect(url_for('home'))
    media_types = Media.query.all()
    return render_template("dashboard.html", title='Site Dashboard', media_types=media_types)


@app.route("/dashboard/add_media_category", methods=['GET', 'POST'])
@login_required
def add_media_cat():
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        form = MediaCatForm()
        if form.validate_on_submit():
            media_type = Media(type=form.type.data)
            db.session.add(media_type)
            db.session.commit()
            flash(f'Media type category was added sucessfully to the database!', 'info')
            return redirect(url_for('dashboard'))
    return render_template("add_media_category.html", title='Add Category', form=form)
