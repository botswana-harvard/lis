from django.db import models
from django.utils.translation import ugettext as _

from lis.base.model.models import BaseLabUuidModel


class SiteLeader (BaseLabUuidModel):

    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=25)

    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=25)

    initials = models.CharField(
        verbose_name=_("Initials"),
        max_length=3)

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return "/bhp_lab_registration/siteleader/%s/" % self.id

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = ['last_name', 'first_name']
        app_label = 'bhp_research_protocol'
