from rant import app, db
from flask import render_template, flash, redirect, url_for
from rant.forms import rantform, deleteform
from rant.models import Post

adminpassword = "admin"

@app.route("/", methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = rantform()

    if form.validate_on_submit():

        
        password = form.password.data
        title = form.title.data
        content = form.content.data
        
        if title == "Title of post." and password == "Password to delete post." and content == "Main text of post.":
            flash('Please change content values.', 'success')
        else:
            flash('You submitted your rant.', 'success')
            # print(title)
            # print(content)
            post1 = Post(title=form.title.data, password=form.password.data, content=form.content.data)
            
            db.session.add(post1)
            db.session.commit()

            # print(Post.query.all())



        return redirect(url_for('home'))

    return render_template("home.html", form=form)


@app.route('/view')
def view():
    posts = Post.query.all()
    return render_template("view.html", posts=posts)


@app.route("/view/<int:post_id>")
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("single_post.html", post=post)



@app.route("/view/<int:post_id>/update", methods=['GET','POST'])
def update_post(post_id):
    form = rantform()
    post = Post.query.get_or_404(post_id)

    if form.validate_on_submit():
        if form.password.data == post.password or form.password.data == adminpassword:
            post.title = form.title.data
            post.content = form.content.data

            db.session.commit()

            flash('Updated!','success')
        else: 
            flash('Incorrect Password.','success')
            

    form.title.data = post.title
    form.content.data = post.content
    form.password.data = "ENTER PASSWORD TO UPDATE"
    

    return render_template("home.html", form=form)



@app.route("/view/<int:post_id>/delete", methods=['GET','POST'])
def delete_post(post_id):
    form = deleteform()
    post = Post.query.get_or_404(post_id)

    if form.validate_on_submit():
        if form.password.data == post.password or form.password.data == adminpassword:
            db.session.delete(post)
            db.session.commit()
            flash('Post Deleted','success')
            return redirect(url_for('view'))
        else:
            abort(403)

    return render_template("delete_post.html", form=form)



@app.route('/about')
def about():
    return 'N/A'