from django import forms
from django.forms.widgets import SelectDateWidget
from datetime import date

from networkapi.news.models import News


class NewsAdminForm(forms.ModelForm):
    date = forms.DateField(
        widget=SelectDateWidget,
        initial=date.today(),
    )

    class Meta:
        model = News
        fields = (
            'headline',
            'outlet',
            'topic',
            'date',
            'link',
            'author',
            'glyph',
            'topic',
            'featured',
        )
