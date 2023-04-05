from django_registration.forms import RegistrationForm
from userBase.models import NormalUser

class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model=NormalUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'profile_picture', 'pan_card')