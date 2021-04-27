"""Module for database entity"""
from utils import db


class Book(db.Model):
    """Class for book entity in database"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True)
    publisher = db.Column(db.String(64))
    author = db.Column(db.String(64), nullable=False)
    published = db.Column(db.Date)
    description = db.Column(db.Text)
    pages = db.Column(db.SmallInteger)
    category = db.Column(db.String(64))

    def __repr__(self):
        return f'Book ({self.title}), {self.author}'
