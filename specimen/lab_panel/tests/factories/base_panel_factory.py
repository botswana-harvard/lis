import factory
from edc.lab.base.model.tests.factories import BaseLabListModelFactory


class BasePanelFactory(BaseLabListModelFactory):
    ABSTRACT_FACTORY = True

    name = factory.Sequence(lambda n: 'panel{0}'.format(n))
