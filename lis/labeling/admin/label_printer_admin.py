from django.contrib import admin

from ..forms import LabelPrinterForm
from ..models import LabelPrinter

from .client_admin import ClientInline


class LabelPrinterAdmin(admin.ModelAdmin):

    form = LabelPrinterForm

    fields = (
        "cups_printer_name",
        "cups_server_hostname",
        "cups_server_ip",
        "default",
    )

    radio_fields = {}
    filter_horizontal = ()
    inlines = [ClientInline, ]
    list_display = ('cups_printer_name', 'cups_server_hostname', 'cups_server_ip', 'default')

admin.site.register(LabelPrinter, LabelPrinterAdmin)
