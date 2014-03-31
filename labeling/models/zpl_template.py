from django.db import models
from lis.base.model.models import BaseLabUuidModel


class ZplTemplate(BaseLabUuidModel):
    """A model of the templates used for formating barcodes in the ZPL template language."""
    name = models.CharField(max_length=50, unique=True)

    template = models.TextField(max_length=250)

    default = models.BooleanField(default=False)

    objects = models.Manager()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.default:
            # set others to False
            self.__class__.objects.all().update(default=False)
        super(ZplTemplate, self).save(*args, **kwargs)

    class Meta:
        app_label = 'labeling'
#         db_table = 'lab_barcode_zpltemplate'