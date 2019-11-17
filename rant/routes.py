from rant import app
from flask import render_template, flash, redirect, url_for
from rant.forms import rantform

@app.route("/", methods=['GET','POST'])
def home():
    form = rantform()
    if form.validate_on_submit():
        flash('You submitted your rant.', 'success')
        return redirect(url_for('home'))
    return render_template("home.html", form=form)