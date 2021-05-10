"""Module for database entity"""
from utils import db


class Book(db.Model):
    """Class for book entity in database"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True)
    publisher = db.Column(db.String(64))
    author = db.Column(db.String(64), nullable=False)
    published = db.Column(db.String(4))
    description = db.Column(db.Text)
    pages = db.Column(db.SmallInteger)
    category = db.Column(db.String(64))
    language = db.Column(db.String(64))
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Book ({self.title}), {self.author}'

    def save(self):
        """Save entity to database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete entity from database"""
        db.session.delete(self)
        db.session.commit()
