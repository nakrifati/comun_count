from django.contrib import admin
from .model import *


class ComAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Com._meta.fields]
#    search_fields = ["com_value"]

    class Meta:
        model = Com

class ComCostAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ComCost._meta.fields]
#    search_fields = ["com_value"]

    class Meta:
        model = ComCost


#admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Com, ComAdmin)
admin.site.register(ComCost, ComCostAdmin)


