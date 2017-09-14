from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from wagtail.wagtailcore.models import Site
from wagtail.wagtailusers.forms import UserCreationForm, UserEditForm

from coss.base.mozillians import BadStatusCode, MozilliansClient, ResourceDoesNotExist


UserModel = get_user_model()


def populate_profile_from_mozillians(instance):
    """Fetches profile data using the mozillians.org API."""

    client = MozilliansClient(settings.MOZILLIANS_API_URL, settings.MOZILLIANS_API_KEY)
    mozillian_user = None
    try:
        mozillian_user = client.lookup_user({'email': instance.email})
    except (ResourceDoesNotExist, BadStatusCode):
        pass

    if mozillian_user:
        instance.username = mozillian_user['username']
        full_name = mozillian_user['full_name']['value']
        instance.first_name, instance.last_name = full_name.split(' ', 1)
        instance.avatar = mozillian_user['photo']['value']
    return instance


class CossUserEditForm(UserEditForm):
    site = forms.ModelChoiceField(queryset=Site.objects,
                                  required=False,
                                  label='Site this account belongs to')
    github = forms.URLField(required=False,
                            label='GitHub Profile URL.')

    def clean(self, *args, **kwargs):
        """Clean method.

        Ensure that only one combination of a valid username and a NULL site exists.
        In SQL NULL != NULL
        """

        cdata = super(CossUserEditForm, self).clean(*args, **kwargs)
        error_msg = ''
        if not (self.instance.is_superuser or self.instance.is_staff) and not cdata.get('site'):
            error_msg = 'You need to associate this account with a site.'

        if error_msg:
            self._errors['site'] = self.error_class([error_msg])
        return cdata

    def save(self, commit=True):
        """Override save method of the form.

        Fetch data from mozillians.org to add the avatar url in the profile.
        """
        obj = super(CossUserEditForm, self).save(commit=False)
        obj = populate_profile_from_mozillians(obj)
        obj.save()
        return obj


class CossUserCreationForm(UserCreationForm):
    site = forms.ModelChoiceField(queryset=Site.objects,
                                  required=False,
                                  label='Site this account belongs to')
    github = forms.URLField(required=False,
                            label='GitHub Profile URL.')

    def __init__(self, *args, **kwargs):
        super(CossUserCreationForm, self).__init__(*args, **kwargs)
        # First, last name and username are not required for the User creation.
        # We will try to populate them through mozillians.org
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['username'].required = False

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

    def save(self, commit=True):
        """Override save method of the form.

        Fetch data from mozillians.org to add the avatar url in the profile.
        """
        obj = super(CossUserCreationForm, self).save(commit=False)
        obj = populate_profile_from_mozillians(obj)
        obj.save()
        return obj
