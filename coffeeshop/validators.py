from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_postcode(value):
    if len(value) != 4:
        raise ValidationError(_("Postcode needs lenght of 4: %(value)s"),
                              code='invalid_lenght',
                              params={'value':value},
                              )
