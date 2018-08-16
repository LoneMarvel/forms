from flask_sqlalchemy import SQLAlchemy
from frm import db
from datetime import datetime

class Movies(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(1200))
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    customer = db.Column(db.String(120))
    category = db.Column(db.String(80))

    def __repr__(self):
        return f'Title -> {self.title}'
