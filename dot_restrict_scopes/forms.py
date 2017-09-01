"""
Django forms for use with the dot-restrict-scopes package.
"""

from django import forms

from oauth2_provider.scopes import get_scopes_backend


class DelimitedListField(forms.MultipleChoiceField):
    """
    Django form field that allows for the use of list widgets with a text field
    containing a delimited list.
    """
    delimiter = ','

    def __init__(self, delimiter = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delimiter = delimiter or self.delimiter

    def prepare_value(self, value):
        # Prepares the value by splitting on the delimiter, trimming leading and
        # trailing whitespace and excluding empty values
        return [p.trim() for p in value.split(self.delimiter) if p.trim()]

    def clean(self, value):
        # Let the parent clean the value first, then join the result using the
        # specified delimiter
        return self.delimiter.join(super().clean(value))


class RestrictedApplicationForm(forms.ModelForm):
    """
    Form for creating or updating a restricted application.
    """
    class Meta:
        exclude = ()
        field_classes = {
            # allowed_scope is a space-delimited list, but we want to present
            # a selection of valid scopes with checkboxes
            'allowed_scope': DelimitedListField(
                choices = get_scopes_backend().get_all_scopes().items(),
                initial = get_scopes_backend().get_default_scopes(),
                delimiter = ' ',
                widget = forms.CheckboxSelectMultiple
            )
        }
