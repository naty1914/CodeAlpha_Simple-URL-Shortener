from app import db


class URL(db.Model):
    """URL model"""
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(6), nullable=False)
    date_created = db.Column(db.DateTime(), nullable=True)
