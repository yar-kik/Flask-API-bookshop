"""Module for testing library views"""

import json
from flask import Response

from tests import AdminCase


class TestBookListApi(AdminCase):
    """Testing the book list test case"""

    def test_book_creation(self) -> None:
        """
        Test API can create a book (with POST request)
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual("Single Book", response.json.get("title"))

    def test_failed_book_creation(self) -> None:
        """
        Test API can't create a book (with POST request) if
        data isn't correct.
        """
        response: Response = self.client.post(
            '/books/', data=json.dumps({"title": "Book title",
                                        "fake_field": "Fake data"}),
            headers=self.headers
        )
        self.assertEqual(response.status_code, 400)

    def test_get_all_books(self) -> None:
        """
        Test API can get a book list (with GET request)
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json.get("books"), list))
        self.assertEqual(1, len(response.json.get("books")))


class TestBookApi(AdminCase):
    """Testing the book get, update and delete test cases"""

    def test_get_book_by_id(self) -> None:
        """
        Test API can get a book by id (with GET request)
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Single Book", response.json.get("title"))

    def test_failed_if_get_book_not_exist(self) -> None:
        """
        Test API can't get a book by id (with GET request) if not exist
        """
        response: Response = self.client.get('/books/123')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': "Not found"})

    def test_edit_book_via_put(self) -> None:
        """
        Test API can update a book (with PUT request)
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.put(
            '/books/1', data=json.dumps({"title": "New title",
                                         "author": "Book author",
                                         "price": 250}),
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual("New title", response.json.get("title"))

    def test_failed_if_edit_book_not_exist_via_put(self) -> None:
        """
        Test API can't edit a book by id (with PUT request) if not exist
        """
        response: Response = self.client.put(
            '/books/123', data=json.dumps({"title": "New title",
                                           "author": "Book author"}),
            headers=self.headers
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': "Not found"})

    def test_failed_if_edit_book_not_valid_via_put(self) -> None:
        """
        Test API can't edit a book by id (with PUT request) if not valid
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.put(
            '/books/1', data=json.dumps({"title": "New title",
                                         "fake_field": "Fake data"}),
            headers=self.headers
        )
        self.assertEqual(response.status_code, 400)

    def test_edit_book_via_patch(self) -> None:
        """
        Test API can update a book (with PATCH request)
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.patch(
            '/books/1', data=json.dumps({"author": "New author"}),
            headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Updated successfully'})

    def test_failed_if_edit_book_not_exist_via_patch(self) -> None:
        """
        Test API can't edit a book by id (with PATCH request) if not exist
        """
        response: Response = self.client.patch(
            '/books/1', data=json.dumps({"author": "New author"}),
            headers=self.headers
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': "Not found"})

    def test_failed_if_edit_book_not_valid_via_patch(self) -> None:
        """
        Test API can't edit a book by id (with PATCH request) if not valid
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.patch(
            '/books/1', data=json.dumps({"fake_field": "Fake data"}),
            headers=self.headers
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_book_by_id(self) -> None:
        """
        Test API can delete a book (with DELETE request)
        """
        response: Response = self.client.post(
            '/books/', data=self.book_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        response: Response = self.client.delete('/books/1',
                                                headers=self.headers)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(response.data)

    def test_failed_if_delete_book_not_exist(self) -> None:
        """
        Test API can't delete a book by id (with DELETE request) if not exist
        """
        response: Response = self.client.delete('/books/123',
                                                headers=self.headers)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': "Not found"})
