from django.db import models

from edc_base.model.models import BaseUuidModel


class ZplTemplate(BaseUuidModel):
    """A model of the templates used for formating barcodes in the ZPL template language."""
    name = models.CharField(max_length=50, unique=True)

    template = models.TextField(max_length=500)

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
