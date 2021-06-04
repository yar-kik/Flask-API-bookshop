"""Module for all mixins"""
from flask import current_app

from library.search import add_to_index, remove_from_index, query_index
from utils import db


# pylint: disable=protected-access
class SearchableMixin:
    """Mixin to implement search functions"""

    @classmethod
    def search(cls, expression):
        """Search by query function"""
        ids = query_index(cls.__tablename__, expression)
        if not ids:
            return cls.query.filter(cls.id.in_(ids))
        when = [(id_, i) for i, id_ in enumerate(ids)]
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id))

    @classmethod
    def before_commit(cls, session):
        """Add changes to session before commit."""
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        """Index object from session after commit"""
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        """Reindex object in db"""
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)


# pylint: disable=no-member
db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)
