from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import Field

from networkapi.people.models import Person


class PersonAdminForm(forms.ModelForm):
    def clean_quote(self):
        cleaned_data = self.cleaned_data
        quote = cleaned_data.get('quote')

        if cleaned_data.get('featured') is True and not quote:
            raise ValidationError(
                Field.default_error_messages['required'],
                code='required',
            )
        return quote

    def clean_bio(self):
        cleaned_data = self.cleaned_data
        bio = cleaned_data.get('bio')

        if cleaned_data.get('featured') is True and not bio:
            raise ValidationError(
                Field.default_error_messages['required'],
                code='required',
            )
        return bio

    class Meta:
        model = Person
        fields = (
            'name',
            'role',
            'location',
            'image',
            'partnership_logo',
            'twitter_url',
            'linkedin_url',
            'internet_health_issues',
            'featured',
            'bio',
            'quote',
        )
