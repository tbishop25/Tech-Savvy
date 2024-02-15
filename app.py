#from bot import chatbot

from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/options")
def options():
	return render_template("options.html")

@app.route("/bot")
def bot():
	return render_template("bot.html")

if __name__ == "__main__":
    app.run(debug=True)
