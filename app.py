from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    player_choice = request.form["choice"]
    bot_choice = random.choice(["Rock", "Paper", "Scissors"])

    if bot_choice == player_choice:
        result = "It's a Tie!"
    elif (
        (bot_choice == "Rock" and player_choice == "Scissors") or
        (bot_choice == "Scissors" and player_choice == "Paper") or
        (bot_choice == "Paper" and player_choice == "Rock")
    ):
        result = "You Lost the Match"
    else:
        result = "You Won the Match"

    return render_template("index.html", result=result, bot=bot_choice, player=player_choice)

if __name__ == "__main__":
    app.run(debug=True)
