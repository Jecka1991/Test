from api.models import CompanyLevels, Big_Boss, Worker, Position
from django.contrib.auth.models import User
import os
import random
import django
from django_seed import Seed

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Company.settings')

django.setup()

seeder = Seed.seeder()


def populate_models():
    seeder.add_entity(CompanyLevels, 5)
    seeder.add_entity(User, 10)
    seeder.add_entity(Big_Boss, 10, {
        'boss_id': lambda x: random.randint(0, 1000),
        'name': lambda x: seeder.faker.first_name(),
        'surname': lambda x: seeder.faker.last_name()
    })
    seeder.add_entity(Position, 10, {
        'position': lambda x: seeder.faker.job()
    })
    seeder.add_entity(Worker, 10, {
        'first_name': lambda x: seeder.faker.first_name(),
        'middle_name': lambda x: seeder.faker.first_name(),
        'last_name': lambda x: seeder.faker.last_name(),
        'work_date': lambda x: seeder.faker.date_this_month(before_today=True, after_today=False),
        'salary': lambda x: random.randint(0, 1000),
        'salary_paid': lambda x: random.randint(1000, 200000),
    })
    inserted_pks = seeder.execute()
    return inserted_pks


if __name__ == "__main__":
    populate_models()