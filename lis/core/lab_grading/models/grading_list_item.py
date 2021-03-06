from django.db import models
from lis.core.lab_reference.models import BaseReferenceListItem
from lis.specimen.lab_test_code.models import TestCode
from .grading_list import GradingList


class GradingListItem(BaseReferenceListItem):

    test_code = models.ForeignKey(TestCode)

    grading_list = models.ForeignKey(GradingList)

    grade = models.IntegerField()

    objects = models.Manager()

    def __unicode__(self):
        return str(self.test_code)

    class Meta:
        app_label = 'lab_grading'
        ordering = ['test_code', 'age_low', 'age_low_unit']
        db_table = 'lab_grading_gradinglistitem'
