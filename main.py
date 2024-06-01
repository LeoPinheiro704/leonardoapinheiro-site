from flask import Flask, render_template, redirect, json
import datetime as dt

app = Flask(__name__)

with open("static/data.json", mode="r") as data_file:
    data = json.load(data_file)


def get_actual_age():
    birthday = dt.datetime(1996, 7, 17)
    today = dt.datetime.now()
    age = (today - birthday) // dt.timedelta(days=365.2425)
    return age


@app.route("/")
def home():
    return render_template("index.html", age=get_actual_age(), data=data)


@app.route('/redirect/<link>')
def redirect_link(link):
    return redirect("http://" + link)


if __name__ == "__main__":
    app.run(debug=True)
