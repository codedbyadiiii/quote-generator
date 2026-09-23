import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Our list of quotes (now we can add to it!)
quotes = [
    {"text": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"text": "Don't let yesterday take up too much of today.", "author": "Will Rogers"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    # If the user submits the form, save the new quote
    if request.method == "POST":
        new_text = request.form.get("quote_text")
        new_author = request.form.get("author_name")
        
        if new_text and new_author:
            quotes.append({"text": new_text, "author": new_author})
            
        return redirect(url_for("home")) # Refresh the page

    # If it's just a normal page load, pick a random quote
    random_quote = random.choice(quotes)
    return render_template("index.html", quote=random_quote)

if __name__ == "__main__":
    app.run(debug=True)