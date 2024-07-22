from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/fortune")
def fortune():
  possible_Fortunes=["you'll step on food", "you'll have a good day", "A cat will follow you everywhere starting now", "a bird poops on you everytime you step outside", "you'll meet a leprachuan", "I cant think of anymore. leave me be", "good night sleep", "stomach ache every 2 hours", "your life is now great.", "you get stuck with 10 gnomes who dont speak a sinlge word of english and only communicate in gibberish who are lactose intolerent and only drink milk."]
  import random
  chosen_number=random.randint(0, len(possible_Fortunes)-1)
  random_fortune= possible_Fortunes[chosen_number]
  return render_template('fortune.html', random_fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True)