from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)


def get_actual_age():
    birthday = dt.datetime(1996, 7, 17)
    today = dt.datetime.now()
    age = (today - birthday) // dt.timedelta(days=365.2425)
    return age


@app.route("/")
def hello_world():
    return render_template("guess.html", age=get_actual_age())


if __name__ == "__main__":
    app.run(debug=True)
