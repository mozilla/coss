from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from coss.opensource_clubs.models import ClubProfile


class ClubProfileAdmin(ModelAdmin):
    menu_label = 'Open Source Clubs Profiles'
    model = ClubProfile


class ProfilesAdminGroup(ModelAdminGroup):
    menu_label = 'User Profiles'
    menu_icon = 'folder-open-inverse'
    items = (ClubProfileAdmin,)


modeladmin_register(ProfilesAdminGroup)
