from library.models import Book
from manage import app
from utils import db

books = {
    "books": [
        {
            "title": "1984",
            "author": "George Orwell",
            "published": 2020,
            "description": "A real masterpiece of antiutopia. You will never forget it",
            "pages": 300,
            "category": "modern novels",
            "language": "russian",
            "price": 125
        },
        {
            "title": "451 Fareinheit",
            "author": "Ray Bradbury",
            "published": 2021,
            "description": "A classic book of antiutopia. Bright characters and plot. Must-read for everyone from everywhere",
            "pages": 255,
            "category": "science fiction",
            "language": "english",
            "price": 115
        },
        {
            "title": "11/22/63",
            "author": "Stephen King",
            "published": 2019,
            "description": "Perfect time-travel book from the all-known author",
            "pages": 825,
            "category": "science fiction",
            "language": "english",
            "price": 255
        },
        {
            "title": "The Dead Zone",
            "author": "Stephen King",
            "published": 2020,
            "description": "Perfect tragic story of person who can predict the future ",
            "pages": 455,
            "category": "science fiction",
            "language": "russian",
            "price": 155
        },
        {
            "title": "Green Mile",
            "author": "Stephen King",
            "published": 2019,
            "description": "The heart-breaking story about innocence prisoner ",
            "pages": 556,
            "category": "fantasy",
            "language": "english",
            "price": 175
        },
        {
            "title": "Harry Potter and the Sorcerer's Stone",
            "author": "Joan K. Rowling",
            "published": 2021,
            "description": "The story of the boy who lived. Must-read to everyone from child to old. The magic is around us",
            "pages": 527,
            "category": "fantasy",
            "language": "english",
            "price": 205
        },
        {
            "title": "Erased. Tom I",
            "author": "Kei Sanbe",
            "published": 2020,
            "description": "Heart touching story about childhood, domestic abuse and relationships between children and mother",
            "pages": 120,
            "category": "manga",
            "language": "english",
            "price": 110
        },
        {
            "title": "The Great Gatsby",
            "author": "Fransis Scott Fitzgerald",
            "published": 2019,
            "description": "The story of the golden age of 1920's full of tragic love and dazzling parties",
            "pages": 320,
            "category": "classic",
            "language": "english",
            "price": 137
        },
        {
            "title": "The Lord of the Ring. The Ring Fellowship",
            "author": "John Ronald R. Tolkien",
            "published": 2019,
            "description": "The first part of longlife travel of Frodo, Sam and others. Classic of the world fantasy",
            "pages": 457,
            "category": "fantasy",
            "language": "english",
            "price": 205
        },
        {
            "title": "Harry Potter and the Hald-Blood Prince",
            "author": "Joan K. Rowling",
            "published": 2020,
            "description": "The sixth part of the boy who lived story. The story is getting darker and darker. Who that mysterious Hald-Blood Prince is? The villain or the hero?",
            "pages": 603,
            "category": "fantasy",
            "language": "english",
            "price": 220
        }
    ]}

books_list = []
for book in books["books"]:
    new_book = Book(title=book["title"],
                    author=book["author"],
                    published=book["published"],
                    description=book["description"],
                    pages=book["pages"],
                    category=book["category"],
                    language=book["language"],
                    price=book["price"])
    books_list.append(new_book)
with app.app_context():
    db.session.add_all(books_list)
    db.session.commit()
