from main import app, db

from flask import render_template
from models import BlogPosts

@app.route('/', methods=['GET', 'POST'])
def info():
    blogposts = BlogPosts.

    return render_template('info.html', blogposts=blogposts)

@app.route('/new_post', methods=['POST'])
def new_post():
    content = request.form['content']
    post = BlogPosts(text=content, subject="Nowy post")
    db.session.add(post)
    db.session.commit()
    return redirect('/')


#app.run(debug=True)