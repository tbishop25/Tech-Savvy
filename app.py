from flask import Flask, render_template, request,redirect, url_for,jsonify
from openai import OpenAI

SUGGESTION_FILE = 'suggestions.txt'

app = Flask(__name__)
app.static_folder = 'static'

client = OpenAI()


parameters = [
    {"role": "system", "content": "You are a kind helpful assistant that assists with problems in Microsoft Word."},
    {"role": "system", "content": "You ONLY assist people with Word."},
    {"role": "system", "content": "If a user asks about anything else, redirect them to Word help."},
]

@app.route("/")
def home():
    style = "style.css"
    return render_template("base.html", style=style)


@app.route("/options")
def options():
	return render_template("options.html")


@app.route("/bot")
def bot():
	return render_template("bot.html")

@app.route('/get', methods=['POST'])
def get_response():
    api_data = request.get_json()
    user_messages = api_data.get('messages', [])
    message = api_data.get('message', '')
    
    if message:
        user_messages.append({"role": "user", "content": message})
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=parameters + user_messages)
        reply = chat.choices[0].message.content
        user_messages.append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    else:
        return jsonify({"error": "Please type before pressing enter or the send button!"})

  
           

      

if __name__ == "__main__":
    app.run(debug=True)
