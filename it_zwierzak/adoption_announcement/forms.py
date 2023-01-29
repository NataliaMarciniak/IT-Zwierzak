from django import forms
from .models import AdoptionApplication


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['your_education', 'number_of_adults_in_the_house', 'number_of_children_in_the_house', 'other_animals',
                  'hours_away_from_home', 'moving_out', 'family_allergies', 'adoption_reason',
                  'animal_name', 'availability', 'feeding_the_animal', 'care_budget',
                  'what_if_you_go_on_vacation']



