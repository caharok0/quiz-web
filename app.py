from flask import Flask, render_template, request, session, redirect, url_for
from db.crud import get_quizes, get_question_after


app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

def start_session(quiz_id = 0):
    session["quiz_id"] = quiz_id
    session["last_question_id"] = 0
    session["correct_ans"] = 0
    session["wrong_ans"] = 0
    session["total"] = 0



@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        quizes = get_quizes()
        return render_template("index.html", quizes_list=quizes) 
    else:
        quiz_id = request.form.get("quiz")
        start_session(quiz_id)
        return redirect(url_for("test"))
        


@app.route("/test", methods = ["GET", "POST"])
def test():
    if "quiz_id" not in session:
        return redirect(url_for("index"))
    return"<h1>test</h1>"

@app.route("/resault")
def resault():
    return"<h1>XD</h1>"

if __name__ == '__main__':
    app.run()