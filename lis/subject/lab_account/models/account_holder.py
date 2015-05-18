from django.db import models
from django.utils.translation import ugettext as _

from edc.base.model.fields import NameField, InitialsField

from lis.base.model.models import BaseLabUuidModel


class AccountHolder(BaseLabUuidModel):

    first_name = NameField(
        verbose_name=_("First name")
    )

    last_name = NameField(
        verbose_name=_("Last name")
    )

    initials = InitialsField()

    comment = models.TextField(
        max_length=100,
        blank=True,)

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return "/lab_account/accountholder/%s/" % self.id

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = ['last_name', 'first_name']
        app_label = 'lab_account'
        db_table = 'bhp_lab_registration_accountholder'
