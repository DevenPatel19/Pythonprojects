from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "thequickbrownfoxjumpedoverthelazyyellowdog"


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/submit', methods=["POST"])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comments'] = request.form['comments']

    return redirect("/result")


@app.route('/result')
def result():

    return render_template(
        "result.html")

if __name__ == "__main__":
    app.run(debug=True)
