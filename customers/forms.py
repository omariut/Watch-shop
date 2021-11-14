from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('name','username')
        

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('name','username')