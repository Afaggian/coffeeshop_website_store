from django.forms.utils import ErrorList
from django.utils.translation import gettext as _

from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from .models import UserDetails
from .widgets import PlaceholderInput, ShowHidePasswordWidget


class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)


# form used for the user to signup
class UserForm(ModelForm):
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
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)

    lastName = forms.CharField(required=False)

    class Meta:
        model = UserDetails
        fields = ['firstName', 'lastName', 'username', 'phone', 'email', 'postcode', 'address']
        error_messages = {
            'username': {
                'unique': _('Please enter another username, this one is taken.'),
            },
        }

    '''
    Function to validate the lenght of the postcode
    def clean_postcode(self):
        postcode = self.cleaned_data.get('postcode')
        if len(postcode) != 4:
            raise forms.ValidationError("Please insert a valid Postcode")
        return postcode'''
