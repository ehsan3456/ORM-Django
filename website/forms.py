django.contrib.auth.forms import UserCreationForm
django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label = '',widget = forms.TextInput(attr={'forms':'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(Label = '',max_Length=100, widget = forms.TextInput(attr={'forms':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(Label = '',max_Length=100, widget = forms.TextInput(attr={'forms':'form-control', 'placeholder': 'Last Name'})) 

    class Meta:
        model = user    
        fields = {'username', 'first_name','last_name'. 'email', 'password1', 'password2'}


def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
