try:
    from edc.device.sync.models import BaseSyncUuidModel as BaseUuidModel
except ImportError:
    from edc.base.model.models import BaseUuidModel


class BaseLabUuidModel(BaseUuidModel):

    class Meta:
        abstract = True