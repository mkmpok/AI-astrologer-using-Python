from flask import Flask, render_template, request
from astrology import generate_prediction, answer_question

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        tob = request.form["tob"]
        place = request.form["place"]

        prediction = generate_prediction(name, dob, tob, place)

        return render_template("result.html",
                               name=name,
                               dob=dob,
                               tob=tob,
                               place=place,
                               prediction=prediction)
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]
    response = answer_question(question)
    return render_template("result.html", prediction=response)

if __name__ == "__main__":
    app.run(debug=True)