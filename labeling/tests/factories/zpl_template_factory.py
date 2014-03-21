from lis.base.model.tests.factories import BaseLabUuidModelFactory

from ...models import ZplTemplate


class ZplTemplateFactory(BaseLabUuidModelFactory):
    FACTORY_FOR = ZplTemplate

    name = 'Template'
    template = 'template'
    default = True
