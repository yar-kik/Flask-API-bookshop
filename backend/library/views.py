"""Module for REST API classes"""

from flask import request, current_app
from flask_restful import Resource
from flask_sqlalchemy import Pagination
from marshmallow import ValidationError
from sqlalchemy.orm import Query

from .schemas import BookSchema
from .models import Book

from utils import db, cache


class BookListApi(Resource):
    """Class for list representation and creating new object"""
    book_schema = BookSchema()

    def get(self):
        """Get list of book objects"""
        page = request.args.get('page', 1, type=int)
        all_books: Query = db.session.query(Book)
        # if request.args:
        #     categories = request.args.getlist("category")
        #     all_books = all_books.filter(Book.category.in_(categories))
        all_books: Pagination = all_books.paginate(
            page, current_app.config['BOOKS_PER_PAGE'], False
        )
        pages_amount = all_books.pages
        data = {"books": self.book_schema.dump(all_books.items, many=True),
                "pages_amount": pages_amount}
        return data

    def post(self):
        """Create new book object"""
        try:
            book = self.book_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        book.save()
        return self.book_schema.dump(book), 201


class BookApi(Resource):
    """Class for detail representation and changing"""
    book_schema = BookSchema()

    def get(self, book_id=None):
        """Get detail information of book"""
        book = cache.get(f"book:{book_id}")
        if not book:
            book = db.session.query(Book).filter_by(id=book_id).first()
        if not book:
            return {'message': "Not found"}, 404
        cache.set(f"book:{book_id}", book,
                  timeout=current_app.config["CACHE_TIMEOUT"])
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
        book.save()
        cache.delete(f"book:{book_id}")
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
        book.save()
        cache.delete(f"book:{book_id}")
        return {'message': 'Updated successfully'}, 200

    def delete(self, book_id):
        """Delete book object"""
        book = db.session.query(Book).filter_by(id=book_id).first()
        if not book:
            return {'message': "Not found"}, 404
        book.delete()
        cache.delete(f"book:{book_id}")
        return '', 204
