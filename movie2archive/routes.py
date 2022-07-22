from flask import render_template, url_for, flash, redirect, request
from movie2archive import app, db, mongo, bcrypt, access_key
from movie2archive.forms import (
    RegistrationForm, LoginForm, MediaCatForm, EditMediaCatForm,
    EditLocationCatForm, LocationCatForm, MovieForm)
from movie2archive.models import User, Movielookup, Media, Location
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
    # movies = mongo.db.movies.find()
    movies = Movielookup.query.all()
    return render_template("collection.html", title='My collection', movies=movies)


@app.route("/dashboard")
@login_required
def dashboard():
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this area.', 'warning')
        return redirect(url_for('home'))
    media_types = Media.query.all()
    location_types = Location.query.all()
    return render_template("dashboard.html", title='Site Dashboard', location_types=location_types, media_types=media_types)


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


@app.route("/dashboard/edit_media_category/<int:media_type_id>/", methods=[
    'GET', 'POST'])
@login_required
def edit_media_cat(media_type_id):
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        media_types = Media.query.get_or_404(media_type_id)
        form = EditMediaCatForm()
        if form.validate_on_submit():
            media_types.type = form.type.data
            db.session.commit()
            flash(f'Media type category was sucessfully updated and added to the database!', 'info')
            return redirect(url_for('dashboard'))
        elif request.method == 'GET':
            form.type.data = media_types.type
            print("form.type.data")
    return render_template("edit_media_category.html", title='Edit Category', form=form)


@app.route("/dashboard/delete_type/<int:media_type_id>/", methods=['POST'])
@login_required
def delete_media_cat(media_type_id):
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        media_types = Media.query.get_or_404(media_type_id)
        db.session.delete(media_types)
        db.session.commit()
        flash(f'Media type category was sucessfully deleted from the database!', 'info')
        return redirect(url_for('dashboard'))


# @app.route("/dashboard")
# @login_required
# def dashboard_location():
#     if str(current_user.id) != access_key:
#         flash(f'{current_user.username}, You are not authorised. to access this area.', 'warning')
#         return redirect(url_for('home'))
#     location_types = Location.query.all()
#     return render_template("dashboard.html", title='Site Dashboard', location_types=location_types)


@app.route("/dashboard/add_location_category", methods=['GET', 'POST'])
@login_required
def add_location_cat():
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        form = LocationCatForm()
        if form.validate_on_submit():
            location_type = Location(location=form.location.data)
            db.session.add(location_type)
            db.session.commit()
            flash(f'Location category was added sucessfully to the database!', 'info')
            return redirect(url_for('dashboard'))
    return render_template("add_location_category.html", title='Add Location', form=form)


@app.route("/dashboard/edit_location_category/<int:location_type_id>/", methods=['GET', 'POST'])
@login_required
def edit_location_cat(location_type_id):
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        location_types = Location.query.get_or_404(location_type_id)
        form = EditLocationCatForm()
        if form.validate_on_submit():
            location_types.location = form.location.data
            db.session.commit()
            flash(f'Location category was sucessfully updated and added to the database!', 'info')
            return redirect(url_for('dashboard'))
        elif request.method == 'GET':
            form.location.data = location_types.location
    return render_template("edit_location_category.html", title='Edit location Category', form=form)


@app.route("/dashboard/delete_location_type/<int:location_type_id>/", methods=['POST'])
@login_required
def delete_location_cat(location_type_id):
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        location_types = Location.query.get_or_404(location_type_id)
        db.session.delete(location_types)
        db.session.commit()
        flash(f'Location category was sucessfully deleted from the database!', 'info')
        return redirect(url_for('dashboard'))


@app.route("/my_collection/add_movie/", methods=['GET', 'POST'])
@login_required
def add_movie():
    # stackoverflow used to help constrict select field, original code
    # modified, source: https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
    media_types = Media.query.all()
    media_list = [(media.id, media.type) for media in media_types]
    location_types = Location.query.all()
    location_list = [(location.id, location.location) for location in location_types]
    form = MovieForm()
    form.media_id.choices = media_list
    form.location_id.choices = location_list
    if form.validate_on_submit():
        movie = Movielookup(
            title=form.title.data,
            notes=form.notes.data,
            media_id=form.media_id.data,
            location_id=form.location_id.data,
            user_id=current_user.id
        )
        db.session.add(movie)
        db.session.commit()
        flash('Your movie was successfully added to your collection.', 'info')
        return redirect(url_for('collection'))
    return render_template("add_movie.html", title='Add a movie to your collection', form=form)