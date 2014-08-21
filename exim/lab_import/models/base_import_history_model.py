from datetime import datetime

from django.db import models

from lis.base.model.models import BaseLabUuidModel


class BaseImportHistoryModel(BaseLabUuidModel):

    start_datetime = models.DateTimeField(default=datetime.today())
    end_datetime = models.DateTimeField(null=True)
    lock_name = models.CharField(max_length=50)
    objects = models.Manager()

    def __unicode__(self):
        return '{0} on {1}'.format(self.start_datetime, self.end_datetime)

    class Meta:
        abstract = True
