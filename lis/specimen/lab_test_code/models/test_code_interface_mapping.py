from django.db import models

from edc_base.model.models import BaseModel

from .test_code import TestCode


class TestCodeInterfaceMapping(BaseModel):

    foreign_test_code = models.CharField(
        verbose_name="Foreign Test Code",
        max_length=15,
        unique=True)

    local_test_code = models.ForeignKey(TestCode, verbose_name="Local Test Code")

    def __str__(self):
        return "%s maps to %s" % (self.foreign_test_code, self.local_test_code)

    class Meta:
        app_label = 'lab_test_code'
        db_table = 'bhp_lab_test_code_testcodeinterfacemapping'
