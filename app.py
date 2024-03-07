

from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    style = "style.css"
    return render_template("base.html", style=style)


@app.route("/options")
def options():
	return render_template("options.html")

@app.route("/t")
def t():
	return render_template("file.html")

@app.route("/bot")
def bot():
	return render_template("bot.html")



if __name__ == "__main__":
    app.run(debug=True)