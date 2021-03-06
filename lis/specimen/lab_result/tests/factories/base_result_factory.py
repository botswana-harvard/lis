import factory
from datetime import datetime
from lis.base.model.tests.factories import BaseLabUuidModelFactory


class BaseResultFactory(BaseLabUuidModelFactory):
    ABSTRACT_FACTORY = True

    result_identifier = factory.Sequence(lambda n: n.rjust(8, '0'))
    result_datetime = datetime.today()
