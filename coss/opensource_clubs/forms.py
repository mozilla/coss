from django.conf import settings

from wagtail.wagtailadmin.forms import WagtailAdminModelForm

from coss.base.mozillians import BadStatusCode, MozilliansClient, ResourceDoesNotExist


class ClubProfileForm(WagtailAdminModelForm):

    def save(self, commit=True):
        """Override save method of the form.

        Fetch data from mozillians.org to add the avatar url in the profile.
        """
        obj = super(ClubProfileForm, self).save(commit=False)
        client = MozilliansClient(settings.MOZILLIANS_API_URL, settings.MOZILLIANS_API_KEY)
        mozillian_user = None
        try:
            mozillian_user = client.lookup_user({'email': obj.user.email})
        except (ResourceDoesNotExist, BadStatusCode):
            pass
        if mozillian_user and mozillian_user['photo']:
            obj.avatar_url = mozillian_user['photo']['value']
        obj.save()
        return obj
