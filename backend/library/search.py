"""Module for search indexing business logic"""
from typing import List

from flask import current_app


def add_to_index(index, model) -> None:
    """Add to search index of elasticsearch"""
    if not current_app.elasticsearch:
        return
    payload = {field: getattr(model, field) for field in model.__searchable__}
    current_app.elasticsearch.index(index=index, doc_type=index,
                                    id=model.id, body=payload)


def remove_from_index(index, model) -> None:
    """Remove from search index of elasticsearch"""
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index, id=model.id)


def query_index(index, query, page, per_page) -> List[int]:
    """Search by query in elasticsearch. Return indexes of items to search."""
    if not current_app.elasticsearch:
        return []
    search = current_app.elasticsearch.search(
        index=index, doc_type=index,
        body={"query": {"multi_match": {"query": query, "fields": ["*"]}},
              "from": (page - 1) * per_page, "size": per_page})
    ids = [int(hit["_id"]) for hit in search["hits"]["hits"]]
    return ids
