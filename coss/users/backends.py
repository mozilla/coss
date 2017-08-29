from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


UserModel = get_user_model()


class CossBackend(ModelBackend):
    """Override Django's default backend.

    When a user authenticates, we need to take into account
    the site the user logs in.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):

        user = super(CossBackend, self).authenticate(request, username, password, **kwargs)

        # check that the user returned is not None
        if not user:
            return user

        if user.is_superuser or user.is_staff:
            return user

        sites_registered = [user.site for user in UserModel.objects.filter(email=user.email)]

        # Do not authenticate users registered to other sites.
        if request.site in sites_registered:
            return user
        return None
