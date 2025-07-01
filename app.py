from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
