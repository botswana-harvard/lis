from django.contrib import admin
from ..models import Order


class OrderAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.order_identifier = self.model.objects.get_identifier()
        if change:
            obj.user_modified = request.user
        save = super(OrderAdmin, self).save_model(request, obj, form, change)
        return save

    #override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):
        if obj:  # In edit mode
            return ('aliquot', 'order_identifier', ) + self.readonly_fields
        else:
            return self.readonly_fields
    fields = ('order_datetime', 'panel', 'aliquot', 'comment', 'dmis_reference', )
    list_display = ('order_identifier', 'order_datetime', 'panel', 'aliquot', 'dmis_reference')
    list_filter = ('order_datetime', 'panel', )
    search_fields = ['order_identifier', 'dmis_reference', 'aliquot__aliquot_identifier', 'aliquot__receive__receive_identifier', 'aliquot__receive__protocol__protocol_identifier']
    date_hierarchy = 'order_datetime'
admin.site.register(Order, OrderAdmin)
