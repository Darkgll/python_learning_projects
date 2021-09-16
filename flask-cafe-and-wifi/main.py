from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = "ANY SECRET KEY YOU WANT"
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafe-wifi.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(250), unique=True, nullable=False)
    map_url = db.Column(db.VARCHAR(500), nullable=False)
    img_url = db.Column(db.VARCHAR(500), nullable=False)
    location = db.Column(db.VARCHAR(500), nullable=False)
    open_time = db.Column(db.VARCHAR(500), nullable=False)
    close_time = db.Column(db.VARCHAR(500), nullable=False)
    coffee_rating = db.Column(db.VARCHAR(500), nullable=False)
    wifi_rating = db.Column(db.VARCHAR(500), nullable=False)
    power_rating = db.Column(db.VARCHAR(500), nullable=False)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe location on Google Maps (URL)', [URL(), DataRequired()])
    image_url = StringField('Photo of Cafe (URL)', [URL(), DataRequired()])
    location_url = StringField('Address (City, street)', [DataRequired()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability',
                               choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')

# db.create_all()


@app.route('/')
def main_page():
    cafes = Cafe.query.all()
    return render_template("index.html", all_cafes=cafes)


@app.route('/add-cafe', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.cafe.data,
            map_url=form.map_url.data,
            img_url=form.image_url.data,
            location=form.location_url.data,
            open_time=form.open_time.data,
            close_time=form.close_time.data,
            coffee_rating=form.coffee_rating.data,
            wifi_rating=form.wifi_rating.data,
            power_rating=form.power_rating.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("main_page"))
    return render_template("add-cafe.html", form=form)


@app.route("/delete/<int:cafe_id>")
def delete_post(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run()
