import factory
from edc.lab.base.model.tests.factories import BaseLabListModelFactory
from edc.lab.lab_common.choices import UNITS


class BaseTestCodeFactory(BaseLabListModelFactory):
    ABSTRACT_FACTORY = True

    code = factory.Sequence(lambda n: 'CODE{0}'.format(n))
    name = factory.Sequence(lambda n: 'NAME{0}'.format(n))
    units = factory.Iterator(UNITS, getter=lambda c: c[0])
    display_decimal_places = 2
