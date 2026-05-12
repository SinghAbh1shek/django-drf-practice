from faker import Faker
import random
from books.models import Author, Book
from django.contrib.auth import get_user_model

User = get_user_model()
fake = Faker()

user = User.objects.first()

if not user:
    user = User.objects.create_user(
        email="test@example.com",
        password="test1234"
    )

genres = [
    "Fantasy", "Sci-Fi", "Romance", "Thriller",
    "Horror", "Mystery", "Adventure", "Drama"
]

authors = []

for _ in range(20):
    author = Author.objects.create(
        name=fake.name()
    )
    authors.append(author)

books = []

for _ in range(100):
    book = Book(
        author=random.choice(authors),
        created_by=user,
        title=fake.sentence(nb_words=4),
        description=fake.text(max_nb_chars=300),
        coverImage=fake.image_url(),
        file=f"https://example.com/books/{fake.uuid4()}.pdf",
        genre=random.choice(genres),
    )

    books.append(book)

Book.objects.bulk_create(books)

print("added")