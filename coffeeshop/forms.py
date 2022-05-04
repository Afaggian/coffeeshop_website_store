from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.forms.utils import ErrorList
from django.utils.translation import gettext as _

from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, PasswordInput, Textarea
from django.contrib.auth.models import User
from .models import UserDetails
from .widgets import PlaceholderInput, ShowHidePasswordWidget


class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)


# form used for the user to signup
class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userForm'
        self.helper.form_mothod = 'post'
        self.helper.form_action = 'signup'
        self.helper.add_input(Submit('submit', 'Sign up', css_class='btn-success'))

        self.helper.layout = Layout(Fieldset('User Information', 'username', 'password', style='color: green;'),
                                    Fieldset('Contact data', 'email', style='color: gree;'),
                                    )

    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # __all__ would include all the fields of the module
        error_messages = {
            'username': {
                'unique': _("Please enter another username, This one is taken"),
            }
        }
        widgets = {
            "username": PlaceholderInput, #forms.TextInput(attrs={'placeholder': 'Username'}),
            "password": ShowHidePasswordWidget,
        }

    def save(self, commit=True, *args,
             **kwargs):  # overwriting the save function so our password hashed before being stored
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get("password"))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m


class UserDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-userDetailsForm'
        self.helper.form_mothod = 'post'
        self.helper.form_action = 'signup'
        self.helper.add_input(Submit('submit', 'Sign up', css_class='btn-success'))

        self.helper.layout = Layout(
            Fieldset('Name', 'username', 'firstName', 'lastName', 'zipcode', style="color: grey;"),
            Fieldset('Contact data', 'email', 'phone', style="color: grey;"),
            Fieldset('Address details', 'address', 'postcode', style="color: grey;"),
                                    )

    class Meta:
        model = UserDetails
        fields = ['firstName', 'lastName', 'username', 'phone', 'email', 'postcode', 'address']
        error_messages = {
            'username': {
                'unique': _('Please enter another username, this one is taken.'),
            },
        }
        widgets = {
            "address": Textarea(attrs={'class': 'form-control'}),
        }

    '''
    Function to validate the lenght of the postcode
    def clean_postcode(self):
        postcode = self.cleaned_data.get('postcode')
        if len(postcode) != 4:
            raise forms.ValidationError("Please insert a valid Postcode")
        return postcode'''
