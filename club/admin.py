from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Club, Interest

club_extra_fieldsets = (
    (None, {
        "fields": (
            "club_description",
            "city",
            "location",
            "activity",
            "interests",
            "affiliated",
        )
    }),
)

class InterestInline(admin.TabularInline):
    model = Interest.club.through

class ClubAdmin(PageAdmin):
    inlines = (
        InterestInline,
    )
    fieldsets = deepcopy(PageAdmin.fieldsets) + club_extra_fieldsets

admin.site.register(Club, ClubAdmin)
