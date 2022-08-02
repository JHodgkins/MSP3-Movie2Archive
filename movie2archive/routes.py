from flask import render_template, url_for, flash, redirect, request
import requests
import json
from bson.objectid import ObjectId
from movie2archive import (
    app, db, mongo, bcrypt, access_key, movie_key, apiurl, headers)
from movie2archive.forms import (
    RegistrationForm, LoginForm, UpdateUserForm, ChangePasswordForm, MediaCatForm, EditMediaCatForm,
    EditLocationCatForm, LocationCatForm, EditionCatForm, EditEditionCatForm, MovieForm, EditMovieForm)
from movie2archive.models import User, Movielookup, Media, Location, Edition
from flask_login import (
    login_user, logout_user, current_user, login_required)
import urllib
import hashlib
from sqlalchemy.sql.functions import func


# Main navigation | Homepage/Landing page
@app.route("/")
@app.route("/home")
def home():
    movies = Movielookup.query.order_by(Movielookup.date_posted.desc()).all()
    return render_template('index.html', movies=movies)


# Main navigation | About page
@app.route("/about")
def about():
    return render_template('about.html', title='About Movie2archive')


# User managment | Regiter for an account
@app.route("/register", methods=['POST', 'GET'])
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


# User managment | Login to site
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
                url_for('profile'))
        else:
            flash(f'login failed, Please try again', 'danger')
    return render_template("login.html", title='Login', form=form)


# User managment | Logout of site
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# User profile | View user details
@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    user_id = current_user.id
    user_movies = Movielookup.query.filter_by(user_id=user_id)
    return render_template("profile.html", title='Profile', user_movies=user_movies)


# User profile | Edit user detail
@app.route("/profile/update/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    form = UpdateUserForm()
    select_user = User.query.get_or_404(id)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Hey {current_user.username}, Your account details were  sucessfully updated.', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        # Defensive check
        if id != current_user.id:
            flash('You cannot edit another persons profile', 'info')
            return redirect(url_for('profile'))
        else:
            form.username.data = current_user.username
            form.email.data = current_user.email
    return render_template("update_profile.html", title='Update your account details', form=form, select_user=select_user)


# User profile | Change password
@app.route("/profile/change_password/<int:id>", methods=['GET', 'POST'])
@login_required
def change_password(id):
    form = ChangePasswordForm()
    select_user = User.query.get_or_404(id)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        select_user.password = hashed_password
        db.session.commit()
        flash('Your password has been changed! Please login again to confirm the password change.', 'success')
        logout_user()
        return redirect(url_for('login'))
    elif request.method == 'GET':
        # Defensive check
        if id != current_user.id:
            flash('You cannot edit another persons account details', 'info')
            return redirect(url_for('profile'))
        else:
            form.password.data = current_user.password
    return render_template('change_password.html', title='Change your  Password', form=form, select_user=select_user)


# My collection | View Most recent entries (20 moviee)
@app.route("/collection/all")
@login_required
def collection_all():
    # movies = mongo.db.movies.find()
    movies = Movielookup.query.order_by(Movielookup.date_posted.desc()).all()
    movie_types = Media.query.order_by(Media.type.asc()).all()
    return render_template("collection_all.html", title='All', default='no movies currently in your collection', movies=movies, movie_types=movie_types)


# My collection | View Movie by media type
@app.route("/collection/<int:media_type_id>/")
@login_required
def collection_cat(media_type_id):
    movies = Movielookup.query.order_by(Movielookup.date_posted.desc()).all()
    movie_types = Media.query.order_by(Media.type.asc()).all()
    m_types = Media.query.get_or_404(media_type_id)
    # mongo_movies = mongo.db.movies.find({"Title": mt})
    mongo_movies = mongo.db.movies.find()
    return render_template("collection_type.html", title=m_types.type, default='No items in this collection', movies=movies, movie_types=movie_types, m_types=m_types, mongo_movies=mongo_movies)


# My collection | View Movie information and details
@app.route("/collection/movie/<int:movie_id>", methods=[
    'GET', 'POST'])
@login_required
def movie_details(movie_id):
    movie = Movielookup.query.get_or_404(movie_id)
    # mongo_movies = mongo.db.movies.find_one({"imdbID": ObjectId(movie.imdbID)})
    mongo_movies = mongo.db.movies.find({"imdbID": movie.imdbID})
    mongo_art = mongo.db.movies.find({"imdbID": movie.imdbID})
    return render_template("movie.html", title=movie.title, movie=movie, mongo_movies=mongo_movies, mongo_art=mongo_art)
    # movies = mongo.db.movies.find()


# My collection | Add Movie
@app.route("/my_collection/add_movie/", methods=['GET', 'POST'])
@login_required
def add_movie():
    # stackoverflow used to help constrict select field, original code
    # modified, source: https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
    media_types = Media.query.all()
    media_list = [(media.id, media.type) for media in media_types]
    location_types = Location.query.all()
    location_list = [(location.id, location.location) for location in location_types]
    edition_types = Edition.query.all()
    edition_list = [(edition.id, edition.edition) for edition in edition_types]
    form = MovieForm()
    form.media_id.choices = media_list
    form.location_id.choices = location_list
    form.edition_id.choices = edition_list

    if form.validate_on_submit():
        # Check if movie already exists
        movie_name = form.title.data.upper()
        check_mongo = mongo.db.movies.find_one({"Title": movie_name})
        
        if check_mongo != None:

            # Construct Movielookup table
            movie = Movielookup(
            title=form.title.data.upper(),
            notes=form.notes.data,
            media_id=form.media_id.data,
            location_id=form.location_id.data,
            edition_id=form.edition_id.data,
            user_id=current_user.id,
            imdbID=check_mongo['imdbID']
            )
            
            # Add to Potgresql
            db.session.add(movie)
            db.session.commit()
            flash('Name match: Your movie was successfully added to your collection.', 'info')
            return redirect(url_for('collection_all'))
        else:
            # call imdb api and return values to be sent to MongoDB
            movie_name = form.title.data
            querystring = {"t": movie_name}
            response = requests.request(
                "GET", apiurl, headers=headers, params=querystring)
            data = [json.loads(response.text)]
            for item in data:
                if item['Response'] == "False":
                    mid = item['Error']
                else:
                    mid = item['imdbID']
                    mtitle = item['Title']
                    mplot = item['Plot']
                    mposter = item['Poster']
                    mactors = item['Actors']
                    mdirector = item['Director']
                    mwriter = item['Writer']
                    mtype = item['Type']
                    mgenre = item['Genre']
                    mreleased = item['Released']
                    mruntime = item['Runtime']
                    mawards = item['Awards']
                    mboxoffice = item['BoxOffice']
                    mimdbrating = item['imdbRating']
                
                if mid != "Movie not found!":
                    # Construct collection for MongoDB
                    movie_mongo = {
                        "Title": mtitle.upper(),
                        "imdbID": mid,
                        "Plot": mplot,
                        "Poster": mposter,
                        "Actors": mactors,
                        "Director": mdirector,
                        "Writer": mwriter,
                        "Type": mtype,
                        "Genre": mgenre,
                        "Released": mreleased,
                        "Runtime": mruntime,
                        "Awards": mawards,
                        "BoxOffice": mboxoffice,
                        "imdbRating": mimdbrating
                    }
                    # Add to MongoDB
                    mongo.db.movies.insert_one(movie_mongo)

            # Construct Movielookup table
            movie = Movielookup(
                title=form.title.data.upper(),
                notes=form.notes.data,
                media_id=form.media_id.data,
                location_id=form.location_id.data,
                edition_id=form.edition_id.data,
                user_id=current_user.id,
                imdbID=mid
            )
            
            # Add to Potgresql
            db.session.add(movie)
            db.session.commit()
            flash('Your movie was successfully added to your collection.', 'info')
            return redirect(url_for('collection_all'))
    return render_template(
        "add_movie.html", title='Add a movie to your collection', form=form)


# My collection | Edit a Movie title
@app.route("/collection/movie/edit_movie/<int:movie_id>/", methods=[
    'GET', 'POST'])
@login_required
def edit_movie(movie_id):
    movies = Movielookup.query.get_or_404(movie_id)
    media_types = Media.query.all()
    media_list = [(media.id, media.type) for media in media_types]
    location_types = Location.query.all()
    location_list = [(location.id, location.location) for location in location_types]
    edition_types = Edition.query.all()
    edition_list = [(edition.id, edition.edition) for edition in edition_types]
    form = EditMovieForm()
    form.media_id.choices = media_list
    form.location_id.choices = location_list
    form.edition_id.choices = edition_list

    if form.validate_on_submit():
        movies.title = form.title.data.upper(),
        movies.notes = form.notes.data,
        movies.media_id = form.media_id.data,
        movies.location_id = form.location_id.data,
        movies.edition_id = form.edition_id.data
        db.session.commit()
        flash(f'Your movie was sucessfully updated with your amended details and will be viewable in your collection!', 'info')
        return redirect(url_for('collection_all'))
    elif request.method == 'GET':
        form.title.data = movies.title
        form.notes.data = movies.notes
        form.media_id.data = movies.media_id
        form.location_id.data = movies.location_id
        form.edition_id.data = movies.edition_id
    return render_template("edit_movie.html", title=movies.title, form=form)


# My collection | Delete a Movie title
@app.route("/collection/movie/delete_movie/<int:movie_id>/", methods=[
 'POST'])
@login_required
def delete_movie(movie_id):
    movies = Movielookup.query.get_or_404(movie_id)  
    db.session.delete(movies)
    db.session.commit()
    flash('Media type category was sucessfully deleted from the database!', 'info')
    return redirect(url_for('collection_all'))


# Admin dashoard view
@app.route("/dashboard")
@login_required
def dashboard():
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this area.', 'warning')
        return redirect(url_for('home'))
    users = User.query.order_by(User.joined.desc()).all()
    movies = Movielookup.query.order_by(Movielookup.date_posted.desc()).all()
    media_types = Media.query.all()
    location_types = Location.query.all()
    edition_types = Edition.query.all()
    return render_template("dashboard.html", title='Admin Dashboard | Movie2Archive', users=users, movies=movies,location_types=location_types, media_types=media_types, edition_types=edition_types)


# Admin dashoard | Add Media type category 
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
    return render_template("add_media_category.html", title='Add a Media type', form=form)

# Admin dashoard | Edit Media type category
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
    return render_template("edit_media_category.html", title=media_types.type, form=form)


# Admin dashoard | Delete Media type category
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


# Admin dashoard | Add location category
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
    return render_template("add_location_category.html", title='Add a location', form=form)


# Admin dashoard | Edit Location category
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
    return render_template(
        "edit_location_category.html", title=location_types.location, form=form)


# Admin dashoard | Delete Location category
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


# Admin dashoard | Add Edition type
@app.route("/dashboard/add_edition_category", methods=['GET', 'POST'])
@login_required
def add_edition_cat():
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        form = EditionCatForm()
        if form.validate_on_submit():
            edition_type = Edition(edition=form.edition.data)
            db.session.add(edition_type)
            db.session.commit()
            flash(f'Edition category was added sucessfully to the database!', 'info')
            return redirect(url_for('dashboard'))
    return render_template("add_edition_category.html", title='Add an edition type', form=form)


# Admin dashoard | Edit Edition type
@app.route("/dashboard/edit_edition_category/<int:edition_type_id>/", methods=['GET', 'POST'])
@login_required
def edit_edition_cat(edition_type_id):
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        edition_types = Edition.query.get_or_404(edition_type_id)
        form = EditEditionCatForm()
        if form.validate_on_submit():
            edition_types.edition = form.edition.data
            db.session.commit()
            flash(f'Edition category was sucessfully updated and added to the database!', 'info')
            return redirect(url_for('dashboard'))
        elif request.method == 'GET':
            form.edition.data = edition_types.edition
    return render_template(
        "edit_edition_category.html", title=edition_types.edition, form=form)


# Admin dashoard | Delete Edition type
@app.route("/dashboard/delete_edition_category<int:edition_type_id>/", methods=['GET', 'POST'])
@login_required
def delete_edition_cat(edition_type_id):
    # Defensive check
    if str(current_user.id) != access_key:
        flash(f'{current_user.username}, You are not authorised. to access this url.', 'warning')
        return redirect(url_for('home'))
    else:
        edition_types = Edition.query.get_or_404(edition_type_id)
        db.session.delete(edition_types)
        db.session.commit()
        flash(f'Edition category was sucessfully deleted from the database!', 'info')
        return redirect(url_for('dashboard'))


# Movie test area code
@app.route("/movietest", methods=['GET', 'POST'])
def movietest():
    movie_name = 'The matrix'
    querystring = {"t": movie_name}
    # responses = []
    response = requests.request("GET", apiurl, headers=headers, params=querystring)
    data = [json.loads(response.text)]

    print(json.dumps(data, indent=2))
    for item in data:
        print(item)
        print(item['Title'])
        print(item['imdbID'])
        mid = item['imdbID']
        mtitle = item['Title']
        mplot = item['Plot']
    print("this is the title:", mtitle)
    print("this is the plot:", mplot)
    movies = data
    print(mtitle)

    return render_template('movietest.html', title='movietest', movies=movies)
