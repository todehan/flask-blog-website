from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    article = dict()
    article["title"] = "Ana Sayfa"
    article["author"] = "todehan"
    return render_template("index.html", article = article)

@app.route("/about")
def about():
    return "About Page"    

@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run(debug=True)
    