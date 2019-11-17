from rant import app
from flask import render_template
from rant.forms import rantform

@app.route("/", methods=['GET','POST'])
def home():
    form = rantform()
    return render_template("home.html", form=form)