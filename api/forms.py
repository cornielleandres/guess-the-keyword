from django						import forms
from django.contrib.auth.forms	import UserCreationForm, UserChangeForm
from .models					import CustomUser
from allauth.account.forms		import SignupForm

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username','first_name', 'last_name', 'email')

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('username','first_name', 'last_name', 'email')

class CustomSignupForm(SignupForm):

	class Meta:
		model = CustomUser
		fields = ('username','first_name', 'last_name', 'email')
