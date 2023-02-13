from django.test import TestCase
from django.contrib.auth.models import User

from adoption_announcement.models import AdoptionApplication, Animal
from adoption_announcement.forms import AdoptionForm


class AdoptionApplicationFormTest(TestCase):

    def test_other_animals(self):
        User.objects.create_user(username='Natalia', first_name='Natalia', last_name='Marciniak',
                                  email='marciniak.natalia95@gmail.com', password='Natalia', is_staff=False,
                                  is_active=True, is_superuser=False)
        user = User.objects.get(id=1)
        Animal.objects.create(name='Puszek', species='pies', gender='Inna', color='czarny', weight='5', age='2',
                              health_and_vaccination='test', history='test', care_taker=user)
        animal = Animal.objects.get(id=1)
        form = AdoptionForm(data={'your_education': 'test1', 'number_of_adults_in_the_house': 12,
                                  'number_of_children_in_the_house': 2, 'other_animals': 'test2',
                                  'hours_away_from_home': 5,
                                  'moving_out': 'test3', 'family_allergies': 'test4', 'adoption_reason': 'test5',
                                  'animal_name': 'test6', 'availability': 16, 'feeding_the_animal': 'test7',
                                  'care_budget': 50,
                                  'what_if_you_go_on_vacation': 'test8', 'applicant': user, 'animal': animal})
        self.assertEqual(form.fields['other_animals'].label, 'Other animals')
        if form.is_valid():
            text = form.cleaned_data['other_animals']
            print(f'Other animals={text}')
            text = form.cleaned_data['moving_out']
            self.assertEqual(form.cleaned_data['moving_out'], 'test3')
            print(f'Moving out={text}')
            text = form.cleaned_data['number_of_children_in_the_house']
            self.assertGreater(form.cleaned_data['number_of_children_in_the_house'], 10)
            print(f'Number of children in the house={text}')

    def test_form_is_not_valid(self):
        User.objects.create_user(username='Natalia', first_name='Natalia', last_name='Marciniak',
                                 email='marciniak.natalia95@gmail.com', password='Natalia', is_staff=False,
                                 is_active=True, is_superuser=False)
        user = User.objects.get(id=1)
        Animal.objects.create(name='Puszek', species='pies', gender='Inna', color='czarny', weight='5', age='2',
                              health_and_vaccination='test', history='test', care_taker=user)
        animal = Animal.objects.get(id=1)
        form = AdoptionForm(data={'your_education': 'test1', 'number_of_adults_in_the_house': 12,
                                  'number_of_children_in_the_house': 2, 'other_animals': 'test2',
                                  'hours_away_from_home': 5,
                                  'moving_out': 'test3', 'family_allergies': 'test4', 'adoption_reason': 'test5',
                                  'animal_name': 'test6', 'availability': 16, 'feeding_the_animal': 'test7',
                                  'care_budget': 50,
                                  'what_if_you_go_on_vacation': 'test8', 'applicant': user, 'animal': animal})
        self.assertFalse(form.is_valid())

    def test_form_is_valid(self):
        User.objects.create_user(username='Natalia', first_name='Natalia', last_name='Marciniak',
                                 email='marciniak.natalia95@gmail.com', password='Natalia', is_staff=False,
                                 is_active=True, is_superuser=False)
        user = User.objects.get(id=1)
        Animal.objects.create(name='Puszek', species='pies', gender='Inna', color='czarny', weight='5', age='2',
                              health_and_vaccination='test', history='test', care_taker=user)
        animal = Animal.objects.get(id=1)
        form = AdoptionForm(data={'your_education': 'test1', 'number_of_adults_in_the_house': 8,
                                  'number_of_children_in_the_house': 2, 'other_animals': 'test2',
                                  'hours_away_from_home': 5,
                                  'moving_out': 'test3', 'family_allergies': 'test4', 'adoption_reason': 'test5',
                                  'animal_name': 'test6', 'availability': 16, 'feeding_the_animal': 'test7',
                                  'care_budget': 50,
                                  'what_if_you_go_on_vacation': 'test8', 'applicant': user, 'animal': animal})
        self.assertTrue(form.is_valid())
