import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        print(name, email, password, next)

    return render_template("home.html")


@app.route('/about')
def about():
    return "about"


if __name__ == '__main__':
    app.run(debug=True)
