from rant import db, app
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.id}','{self.date_posted}','{self.title}')"