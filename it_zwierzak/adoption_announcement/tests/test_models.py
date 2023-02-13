from django.test import TestCase
from django.contrib.auth.models import User
from adoption_announcement.models import Animal


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='Natalia', first_name='Natalia', last_name='Marciniak',
                                 email='marciniak.natalia95@gmail.com', password='Natalia', is_staff=False,
                                 is_active=True, is_superuser=False)
        user = User.objects.get(id=1)
        Animal.objects.create(name='Puszek', species='pies', gender='Inna', color='czarny', weight='5', age='2',
                              health_and_vaccination='test', history='test', care_taker=user)
        pass

    def test_name_label(self):
        animal = Animal.objects.get(id=1)
        field_label = animal._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        print(animal.name)

    def test_name(self):
        animal = Animal.objects.get(id=1)
        field_value = animal.name
        print(animal.name)
        self.assertEqual(field_value, 'Puszek')

    def test_name_max_length(self):
        animal = Animal.objects.get(id=1)
        max_length = animal._meta.get_field('name').max_length
        animal_name = animal.name
        self.assertLess(len(animal_name), max_length)

    def test_species(self):
        animal = Animal.objects.get(id=1)
        field_value = animal.species
        print(animal.species)
        self.assertEqual(field_value, 'pies')

    def test_gender(self):
        animal = Animal.objects.get(id=1)
        field_label = animal.gender
        print(animal.gender)
        self.assertEqual(field_label, 'Inna')

    def test_color(self):
        animal = Animal.objects.get(id=1)
        field_value = animal.color
        print(animal.color)
        self.assertEqual(field_value, 'czarny')

    def test_weight(self):
        animal = Animal.objects.get(id=1)
        field_value = animal.weight
        print(animal.weight)
        self.assertEqual(field_value, 5)

    def test_age(self):
        animal = Animal.objects.get(id=1)
        field_value = animal.age
        print(animal.age)
        self.assertEqual(field_value, 2)

    def test_history(self):
        animal = Animal.objects.get(id=1)
        field_value = animal.history
        print(animal.history)
        self.assertEqual(field_value, 'test')

    def test_care_taker(self):
        user = User.objects.get(id=1)
        field_value = user.username
        print(user.username)
        self.assertEqual(field_value, 'Natalia')

    def test_health_and_vaccination(self):
        animal = Animal.objects.get(id=1)
        health_and_vaccination = animal.health_and_vaccination
        print(animal.health_and_vaccination)
        self.assertEqual(health_and_vaccination, 'test')

    def test_change_name(self):
        animal = Animal.objects.get(id=1)
        animal.name = 'Bubuś'
        animal1 = Animal.objects.get(id=1)
        self.assertNotEqual(animal.name, animal1.name)
        name_changed = animal.name
        print(animal.name)
        self.assertEqual(name_changed, 'Bubuś')

