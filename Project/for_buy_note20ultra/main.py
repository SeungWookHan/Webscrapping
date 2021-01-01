from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_All, get_I

get_I()
app = Flask("Note20_Ultra")


@app.route("/")
def home():
    datas = get_All()
    return render_template("home.html", datas=datas)


app.run(host="0.0.0.0")