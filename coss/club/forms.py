from django.forms import ModelForm
from coss.club.models import ClubRegistration


class ClubRegistrationForm(ModelForm):
    class Meta:
        model = ClubRegistration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClubRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
