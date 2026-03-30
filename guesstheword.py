# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# List of words
words = ["python", "computer", "programming", "developer", "keyboard", "internet",
    "laptop", "monitor", "software", "hardware", "database", "network",
    "algorithm", "function", "variable", "compiler", "debugging",
    "application", "technology", "science", "education", "engineering",
    "mathematics", "physics", "chemistry", "biology", "history",
    "geography", "language", "dictionary", "knowledge","wisdom", "creativity", "imagination", "innovation", "inspiration",  
    "motivation", "success", "failure", "challenge", "opportunity", "adventure", "exploration", "discovery", "curiosity", "passion",
    "determination", "perseverance", "resilience", "courage", "confidence", "self-esteem", "happiness", "friendship", "family", "love"  
]

word = random.choice(words)
attempts = 3

def hide_letters(word):
    hidden = ""
    for letter in word:
        hidden += "_" if random.random() < 0.5 else letter
    return hidden

hidden_word = hide_letters(word)

@app.route("/")
def index():
    return render_template("index.html", hidden_word=hidden_word, attempts=attempts)

@app.route("/check", methods=["POST"])
def check():
    global attempts, word
    guess = request.json.get("guess", "").lower()
    if guess == word:
        return jsonify({"result": "correct", "word": word})
    else:
        attempts -= 1
        if attempts <= 0:
            return jsonify({"result": "gameover", "word": word})
        else:
            return jsonify({"result": "wrong", "attempts": attempts})

if __name__ == "__main__":
    app.run(debug=True)