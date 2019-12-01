from rant import app
from flask import render_template, flash, redirect, url_for
from rant.forms import rantform



@app.route("/", methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = rantform()

    if form.validate_on_submit():

        flash('You submitted your rant.', 'success')
        title = form.title.data
        content = form.content.data
        print(title)
        print(content)

        return redirect(url_for('home'))

    return render_template("home.html", form=form)


@app.route('/view')
def view():
    return 'N/A'


@app.route('/about')
def about():
    return 'N/A'