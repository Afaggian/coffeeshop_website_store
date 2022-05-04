from django.forms import ValidationError, BaseInlineFormSet


# doesn't let the user submit an empty form
class BaseOrderFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return
        if not self.forms[0].has_changed():
            raise ValidationError('Please add at least one item to proceed')
