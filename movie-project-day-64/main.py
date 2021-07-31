from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Any secret key you want'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gll-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class EditMovie(FlaskForm):
    rating = StringField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


# api key from TMDB
api_key = ""


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for movie in range(len(all_movies)):
        all_movies[movie].ranking = len(all_movies) - movie
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add_movie", methods=['POST', 'GET'])
def add():
    edit_form = AddMovie()
    if edit_form.validate_on_submit():
        movie_title = edit_form.title.data
        print(movie_title)
        parameters = {
            'query': movie_title,
            'api_key': api_key
        }
        response = requests.get(url='https://api.themoviedb.org/3/search/movie', params=parameters)
        movies_results = response.json()['results']
        for item in movies_results:
            print(item)
        return render_template('select.html', movies=movies_results)
    return render_template('add.html', form=edit_form)


@app.route('/get-movie-details')
def get_movie_details():
    movie_id = request.args.get('movie_id')
    print(movie_id)
    parameters = {
        'api_key': api_key
    }
    response = requests.get(url=f'https://api.themoviedb.org/3/movie/{movie_id}', params=parameters)
    movie_details = response.json()
    print(movie_details)
    title = movie_details['original_title']
    img_url = f"https://image.tmdb.org/t/p/w780{movie_details['backdrop_path']}"
    year = request.args.get('movie_year')
    description = request.args.get('movie_description')
    new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', movie_id=new_movie.id))


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    edit_form = EditMovie()
    movie_id = request.args.get('movie_id')
    movie_to_update = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form, movie=movie_to_update)


@app.route("/delete_movie")
def del_movie():
    movie_id = request.args.get('movie_id')
    print(movie_id)
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
