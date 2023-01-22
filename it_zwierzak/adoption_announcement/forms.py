from django import forms
from .models import AdoptionApplication


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['your_education', 'number_of_adults_in_the_house', 'number_of_children_in_the_house', 'other_animals',
                  'hours_away_from_home', 'what_about_moving', 'someone_is_allergic', 'why_adoption',
                  'specific_animal_to_adopt', 'hours_of_interaction', 'feeding_the_animal', 'animal_maintenance',
                  'what_if_you_go_on_vacation']

        # def clean_number_of_adults_in_the_house(self):
        #     clean_number = self.clean_number_of_adults_in_the_house['number_of_adults_in_the_house']
        #     if clean_number.is_valid():
        #         return clean_number
        #     else:
        #         raise forms.ValidationError('Niepoprawna liczba osób dorosłych!')

