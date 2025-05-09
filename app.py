from flask import Flask, render_template
import pandas as pd

brasileirao_matches = pd.read_csv("data/clean/brasileirao_matches.csv").to_dict(orient="records")
print(brasileirao_matches)

app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html", matches=brasileirao_matches)