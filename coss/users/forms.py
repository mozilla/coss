from django import forms
from django.contrib.auth import get_user_model

from wagtail.wagtailcore.models import Site
from wagtail.wagtailusers.forms import UserCreationForm, UserEditForm


UserModel = get_user_model()


class CossUserEditForm(UserEditForm):
    site = forms.ModelChoiceField(queryset=Site.objects,
                                  required=False,
                                  label='Site this account belongs to')

    def clean(self, *args, **kwargs):
        """Clean method.

        Ensure that only one combination of a valid username and a NULL site exists.
        In SQL NULL != NULL
        """

        cdata = super(CossUserEditForm, self).clean(*args, **kwargs)
        error_msg = ''
        if not self.instance.is_superuser or not self.instance.is_staff and not cdata.get('site'):
            error_msg = 'You need to associate this account with a site.'

        if ((self.instance.is_superuser or self.instance.is_staff) and
            cdata.get('username') != self.instance.username and
                UserModel.objects.filter(username=cdata.get('username'),
                                         site__isnull=True).exists()):
            error_msg = 'There is already a global account for this username.'

        if error_msg:
            self._errors['site'] = self.error_class([error_msg])
        return cdata


class CossUserCreationForm(UserCreationForm):
    site = forms.ModelChoiceField(queryset=Site.objects,
                                  required=False,
                                  label='Site this account belongs to')

    def clean(self, *args, **kwargs):
        """Clean method.

        Ensure that only one combination of a valid username and a NULL site exists.
        In SQL NULL != NULL
        """
        cdata = super(CossUserCreationForm, self).clean(*args, **kwargs)
        error_msg = ''

        # Do not allow non-admin accounts with an empty site entry
        if not cdata.get('is_superuser') and not cdata.get('site'):
            # raise ValidationError('You need to associate this account with a site.')
            error_msg = 'You need to associate this account with a site.'

        if UserModel.objects.filter(username=cdata.get('username'), site__isnull=True).exists():
            error_msg = 'There is already a global account for this username.'

        if error_msg:
            self._errors['site'] = self.error_class([error_msg])

        return cdata
