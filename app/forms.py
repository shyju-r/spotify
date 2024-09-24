from django.forms import Form,ModelForm
from app.models import Signupmodel,Songmodel,CategoryModel,Subcategorymodel


class SignupForm(ModelForm):
    class Meta:
        model=Signupmodel
        fields="__all__"
        
class ForgetpassForm(ModelForm):
    class Meta:
        model=Signupmodel
        fields=["password"]
        
class SongForm(ModelForm):
    class Meta:
        model=Songmodel
        fields="__all__"
             
class SongupdateForm(ModelForm):
    class Meta:
        model=Songmodel
        fields="__all__"
        
class CategoryForm(ModelForm):
    class Meta:
        model=CategoryModel
        fields="__all__"
        
class subcategoryForm(ModelForm):
    class Meta:
        model=Subcategorymodel
        fields="__all__"