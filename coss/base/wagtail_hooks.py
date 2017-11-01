from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail.wagtailcore import hooks

from coss.opensource_clubs.models import ClubProfile


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{0}">', static('css/admin.css'))


class ClubProfileAdmin(ModelAdmin):
    menu_label = 'Open Source Clubs Profiles'
    model = ClubProfile
    list_display = ('get_full_name', 'get_username', 'is_captain', 'is_mentor',)

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    def get_username(self, obj):
        return obj.user.username

    get_full_name.short_description = 'Full Name'
    get_username.short_description = 'Username'


class ProfilesAdminGroup(ModelAdminGroup):
    menu_label = 'User Profiles'
    menu_icon = 'folder-open-inverse'
    items = (ClubProfileAdmin,)


modeladmin_register(ProfilesAdminGroup)
