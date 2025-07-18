from flask import Flask, render_template, request
from madlibs import generate_story

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    story = None
    if request.method == "POST":
        words = {
            "noun": request.form.get("noun"),
            "verb": request.form.get("verb"),
            "adjective": request.form.get("adjective"),
            "place": request.form.get("place"),
            "person": request.form.get("person")
        }
        story = generate_story(words)
    return render_template("index.html", story=story)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

