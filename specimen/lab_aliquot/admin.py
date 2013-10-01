from django.contrib import admin
from edc.base.admin.admin import BaseModelAdmin
from edc.lab.lab_aliquot.models import Aliquot


class AliquotAdmin(BaseModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.aliquot_identifier = self.model.objects.get_identifier(
                parent_identifier=request.POST.get('parent_identifier'),
                aliquot_type=request.POST.get('aliquot_type'),
                )
        save = super(AliquotAdmin, self).save_model(request, obj, form, change)
        return save

    def get_readonly_fields(self, request, obj=None):
        if obj:  # In edit mode
            return ('aliquot_type', 'receive', 'original_measure',) + self.readonly_fields
        else:
            return self.readonly_fields
    fields = ('aliquot_identifier', 'receive', 'aliquot_type', 'medium', 'original_measure',
              'current_measure', 'measure_units', 'aliquot_condition', 'status', 'comment')
    list_display = ('aliquot_identifier', 'aliquot_type', 'original_measure', 'current_measure',
                    'measure_units', 'aliquot_condition', 'receive')
    readonly_fields = ('aliquot_identifier',)
admin.site.register(Aliquot, AliquotAdmin)
