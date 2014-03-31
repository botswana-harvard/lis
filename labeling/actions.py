from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured

from .classes import Label, QuerysetLabel, AliquotLabel
from .exceptions import PrinterException
from .models import LabelPrinter


def print_test_label(modeladmin, request, queryset):

    #get printer
    label_printer = LabelPrinter.objects.filter(default=True)
    if label_printer:
        # get default printer, or the first default printer
        label_printer = LabelPrinter.objects.filter(default=True)[0]
        # templates to print
        for zpl_template in queryset:
            label = Label(template=zpl_template)
            label.print_label()
    modeladmin.message_user(request, label.message)

print_test_label.short_description = "Print test label to default printer "


def print_requisition_label(modeladmin, request, requisitions):
    queryset_label = QuerysetLabel()
    if not modeladmin.label_template_name:
        raise ImproperlyConfigured('{0} attribute \'label_template_name\' must be set. '
                                   'Got None.'.format(unicode(modeladmin.__class__.__name__)))
    for requisition in requisitions:
        if requisition.is_receive:
            queryset_label.print_label(
                requisition=requisition,
                remote_addr=request.META.get('REMOTE_ADDR'),
                template=modeladmin.label_template_name)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Requisition {0} has not been received. Labels '
                                 'cannot be printed until the specimen is '
                                 'received.'.format(requisition.requisition_identifier,))
print_requisition_label.short_description = "LABEL: print requisition label"


def print_aliquot_label(modeladmin, request, aliquots):
    """ Prints an aliquot label."""
    aliquot_label = AliquotLabel()
    try:
        for aliquot in aliquots:
            aliquot_label.print_label_for_aliquot(request, aliquot)
    except PrinterException as e:
        messages.add_message(request, messages.ERROR, e.value)
print_aliquot_label.short_description = "LABEL: print aliquot label"