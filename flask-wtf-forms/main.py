from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(), InputRequired()])
    pwd = PasswordField(label='Password', validators=[Length(8), InputRequired()])
    submit = SubmitField(label='Log In')


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app


app = create_app()
app.secret_key = "some super secret string"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.pwd.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
