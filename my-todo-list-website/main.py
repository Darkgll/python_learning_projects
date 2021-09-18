from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = "ANY SECRET KEY YOU WANT"
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    todo_posts = relationship("TODOPost", back_populates="user")


class TODOPost(db.Model):
    __tablename__ = "todo_posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="todo_posts")
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.String(250), nullable=False)
    completed = db.Column(db.Integer, nullable=False)


db.create_all()


class CreateTODOForm(FlaskForm):
    body = StringField("TODO", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Enter")


@app.route("/")
def main_page():
    todos = TODOPost.query.all()
    return render_template("index.html", all_todos=todos)


@app.route("/todo", methods=["GET", "POST"])
def add_todo():
    todo_form = CreateTODOForm()
    if todo_form.validate_on_submit():
        new_todo = TODOPost(
            body=todo_form.body.data,
            completed=0,
            user=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("main_page"))
    return render_template("add-todo.html", form=todo_form)


@app.route("/edit-todo/<int:todo_id>", methods=["GET", "POST"])
def edit_todo(todo_id):
    todo = TODOPost.query.get(todo_id)
    edit_form = CreateTODOForm(
        author=current_user,
        body=todo.body
    )
    if edit_form.validate_on_submit():
        todo.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("main_page", post_id=todo.id))
    return render_template("add-todo.html", form=edit_form)


@app.route("/todo-done/<int:todo_id>")
def todo_done(todo_id):
    todo = TODOPost.query.get(todo_id)
    todo.completed = 1
    db.session.commit()
    return redirect(url_for('main_page'))


@app.route("/todo-undone/<int:todo_id>")
def todo_undone(todo_id):
    todo = TODOPost.query.get(todo_id)
    todo.completed = 0
    db.session.commit()
    return redirect(url_for('main_page'))


@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first():
            flash("Account with this email already exist.")
            return redirect(url_for('register'))
        new_user = User(
            email=register_form.email.data,
            password=generate_password_hash(register_form.password.data, method='pbkdf2:sha256', salt_length=8),
            name=register_form.name.data
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("main_page"))
    return render_template("register.html", form=register_form)


@app.route('/login', methods=["GET", "POST"])
def login():
    register_form = LoginForm()
    if register_form.validate_on_submit():
        user_email = register_form.email.data
        user_password = register_form.password.data

        user_data = User.query.filter_by(email=user_email).first()
        if user_data:
            user_hash = user_data.password

            if check_password_hash(pwhash=user_hash, password=user_password):
                login_user(user_data)
                return redirect(url_for('main_page'))
            else:
                flash('Wrong password.')
                return render_template('login.html', form=register_form)
        else:
            flash("This email doesn't exist in the database, please try again.")
            return render_template('login.html', form=register_form)
    return render_template('login.html', form=register_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page'))


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo_to_delete = TODOPost.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(debug=True)
