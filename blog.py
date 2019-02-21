from flask import Flask,render_template,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")   

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/article/<string:id>")
def article(id):
    return render_template("article.html")

if __name__ == "__main__":
    app.run(debug=True)
    