from django.forms import Form,ModelForm
from app.models import Signupmodel


class SignupForm(ModelForm):
    class Meta:
        model=Signupmodel
        fields="__all__"
        
class ForgetpassForm(ModelForm):
    class Meta:
        model=Signupmodel
        fields=["password"]