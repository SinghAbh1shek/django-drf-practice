from home.models import Author
from faker import Faker
fake = Faker()

for i in range(1, 100):
    Author.objects.create(name = fake.name())