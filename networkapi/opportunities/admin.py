from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.opportunities.models import Opportunity


class OpportunityAdmin(SortableAdmin):
    sortable_change_list_template = (
        'shared/adminsortable_change_list_custom.html'
    )

admin.site.register(Opportunity, OpportunityAdmin)
