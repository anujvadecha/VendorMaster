from django_registration.forms import RegistrationForm
from userBase.models import NormalUser

class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model=NormalUser