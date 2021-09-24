from flask import Flask, flash, request, redirect, url_for, render_template
from colorthief import ColorThief
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os

# UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

app = Flask(__name__)
app.config['SECRET_KEY'] = "Any Secret Key"
app.config['UPLOAD_FOLDER'] = 'static/'
Bootstrap(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def main_page():
    file = "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2070&q=80"
    return render_template("index.html", name=file)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('main_page'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        full_image_path = f"static/{file.filename}"
        color_thief = ColorThief(full_image_path)
        palette = color_thief.get_palette(color_count=10)
        print(palette)
        return render_template("index.html", name=f"static/{file.filename}", all_colours=palette)


if __name__ == "__main__":
    app.run()
