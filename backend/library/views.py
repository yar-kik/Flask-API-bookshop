"""Module for REST API classes"""

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from .schemas import BookSchema
from .models import Book

from utils import db, cache


class BookListApi(Resource):
    """Class for list representation and creating new object"""
    book_schema = BookSchema()

    def get(self):
        """Get list of book objects"""
        all_books = db.session.query(Book).all()
        return self.book_schema.dump(all_books, many=True)

    def post(self):
        """Create new book object"""
        try:
            book = self.book_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(book)
        db.session.commit()
        return self.book_schema.dump(book), 201


class BookApi(Resource):
    """Class for detail representation and changing"""
    book_schema = BookSchema()

    def get(self, book_id=None):
        """Get detail information of book"""
        book = cache.get(book_id)
        if not book:
            book = db.session.query(Book).filter_by(id=book_id).first()
        if book:
            cache.set(book_id, book, timeout=9 * 60)
        else:
            return {'message': "Not found"}, 404
        return self.book_schema.dump(book)

    def put(self, book_id):
        """Update book object. Should be all fields, else some information will
        lost"""
        book = db.session.query(Book).filter_by(id=book_id).first()
        if not book:
            return {'message': "Not found"}, 404
        try:
            book = self.book_schema.load(request.json, instance=book,
                                         session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(book)
        db.session.commit()
        cache.delete(book_id)
        return self.book_schema.dump(book), 200

    def patch(self, book_id):
        """Update book object. Could be only one field"""
        book = db.session.query(Book).filter_by(id=book_id).first()
        if not book:
            return {'message': "Not found"}, 404
        try:
            book = self.book_schema.load(request.json,
                                         instance=book,
                                         partial=True,
                                         session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(book)
        db.session.commit()
        cache.delete(book_id)
        return {'message': 'Updated successfully'}, 200

    def delete(self, book_id):
        """Delete book object"""
        book = db.session.query(Book).filter_by(id=book_id).first()
        if not book:
            return {'message': "Not found"}, 404
        db.session.delete(book)
        db.session.commit()
        cache.delete(book_id)
        return '', 204
