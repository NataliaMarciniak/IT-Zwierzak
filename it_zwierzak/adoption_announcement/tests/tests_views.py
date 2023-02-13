from django.test import TestCase
from django.shortcuts import render
from django.urls import reverse
from http import HTTPStatus

from adoption_announcement.models import AdoptionApplication
from adoption_announcement.forms import AdoptionForm


class AdoptionApplicationViewTest(TestCase):

    def test_post_method(self):
        response = self.client.post("/adoption_form/1", data={"your_education": "test", "number_of_adults_in_the_house": 1, "number_of_children_in_the_house": 0,
            "other_animals": "test", "hours_away_from_home": 2, "moving_out": "test", "family_allergies": "test",
            "adoption_reason": "test", "animal_name": "test", "availability": 1, "feeding_the_animal": "test",
            "care_budget": 541, "what_if_you_go_on_vacation": "test"}, follow=True)
        print(response)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/adoption_form/1')
        self.assertEqual(response.status_code, 200)
