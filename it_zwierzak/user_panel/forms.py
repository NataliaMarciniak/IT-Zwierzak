from .models import Profile #import Profile from models.py

# Create your forms here.
class NewUserForm(UserCreationForm):
    ...

class UserForm(forms.ModelForm):
   ...

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('products',)