from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Club, ClubTopic

club_extra_fieldsets = (
    (None, {
        "fields": (
            "club_description",
            "city",
            "location",
            "activity",
            "affiliated",
        )
    }),
)

class ClubAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + club_extra_fieldsets

admin.site.register(Club, ClubAdmin)
admin.site.register(ClubTopic)
