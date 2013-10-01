from datetime import *
from django.contrib import admin
from edc.base.admin.admin import BaseModelAdmin
from edc.lab.lab_order.models import Order
from .models import Result


class ResultAdmin(BaseModelAdmin):

    def change_view(self, request, object_id, extra_context=None):

        response = super(ResultAdmin, self).change_view(request, object_id, extra_context)

        oResult = Result.objects.get(id__exact=object_id)

        if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
            response['Location'] = oResult.get_document_url()
        return response

    # override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):
        if obj:  # In edit mode
            return ('order',) + self.readonly_fields
        else:
            return self.readonly_fields

    # override, limit dropdown in add_view to id passed in the URL
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "order":
            kwargs["queryset"] = Order.objects.filter(id__exact=request.GET.get('order', 0))
        return super(ResultAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('result_identifier', 'receive_identifier', 'subject_identifier', 'result_datetime', 'release_status', 'order',)
    search_fields = ('result_identifier', 'release_status', 'receive_identifier', 'subject_identifier')
    list_filter = ('release_status', 'result_datetime', 'release_status')
    list_per_page = 15

admin.site.register(Result, ResultAdmin)
